import requests
from bs4 import BeautifulSoup
import markdownify
from datetime import datetime
import re
from urllib.parse import urljoin, urlparse
import time

def clean_content(soup_content):
    """Remove unwanted elements from content"""
    # Remove script, style, and other non-content tags
    for element in soup_content.find_all(['style', 'script', 'noscript', 'nav', 'header', 'footer', 'aside']):
        element.decompose()
    
    # Remove elements with certain classes that indicate non-content
    for element in soup_content.find_all(class_=['sidebar', 'navigation', 'menu', 'breadcrumb', 'toc']):
        element.decompose()
        
    return soup_content

def extract_content(soup):
    """Extract main content from page"""
    # Try multiple selectors for documentation content
    selectors = [
        'main article',
        'main',
        'article', 
        '[role="main"]',
        '.docs-content',
        '.content-wrapper',
        '.documentation-content',
        '[data-testid="content"]'
    ]
    
    for selector in selectors:
        content = soup.select_one(selector)
        if content and len(content.get_text(strip=True)) > 200:
            return clean_content(content)
    
    # Fallback: find largest content div
    all_elements = soup.find_all(['div', 'section', 'main', 'article'])
    if all_elements:
        content = max(all_elements, key=lambda e: len(e.get_text(strip=True)))
        if len(content.get_text(strip=True)) > 200:
            return clean_content(content)
    
    return None

def extract_claude_code_links(soup, base_url):
    """Extract all Claude Code related links from the page"""
    links = set()
    
    # Look for links in navigation and content
    for a in soup.find_all('a', href=True):
        href = a['href']
        
        # Skip anchors and external links
        if href.startswith('#') or href.startswith('http') and 'anthropic.com' not in href:
            continue
        
        # Make absolute URL
        full_url = urljoin(base_url, href)
        
        # Only include Claude Code related pages
        if '/claude-code/' in full_url and full_url.startswith('https://docs.anthropic.com'):
            # Skip certain types of pages
            if any(skip in full_url for skip in ['#', '.pdf', '.zip', 'changelog', 'release-notes']):
                continue
            links.add(full_url)
    
    return links

def scrape_page(url, session):
    """Scrape a single page"""
    try:
        print(f"Scraping: {url}")
        response = session.get(url, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        content = extract_content(soup)
        
        if not content:
            print(f"  No content found for {url}")
            return None, set()
        
        # Convert to markdown
        markdown = markdownify.markdownify(
            str(content), 
            heading_style="ATX",
            convert=['p', 'div', 'span', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 
                    'ul', 'ol', 'li', 'a', 'code', 'pre', 'blockquote', 
                    'strong', 'em', 'b', 'i', 'table', 'tr', 'td', 'th']
        )
        
        # Clean up the markdown
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)
        markdown = re.sub(r'^\s*\n', '', markdown, flags=re.MULTILINE)
        
        # Extract links for recursive scraping
        links = extract_claude_code_links(soup, url)
        
        return markdown, links
        
    except Exception as e:
        print(f"  Error scraping {url}: {str(e)}")
        return None, set()

def scrape_claude_docs_recursive():
    """Recursively scrape all Claude Code documentation"""
    base_url = "https://docs.anthropic.com/en/docs/claude-code/overview"
    visited = set()
    to_visit = {base_url}
    all_content = {}
    
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (compatible; Claude-Code-Docs-Scraper/2.0)'
    })
    
    while to_visit:
        url = to_visit.pop()
        if url in visited:
            continue
        
        visited.add(url)
        content, new_links = scrape_page(url, session)
        
        if content:
            # Extract page title from URL
            page_name = url.split('/')[-1].replace('-', ' ').title()
            all_content[url] = {
                'title': page_name,
                'content': content
            }
            
            # Add new links to visit
            for link in new_links:
                if link not in visited:
                    to_visit.add(link)
        
        # Be polite to the server
        time.sleep(0.5)
    
    return all_content

def compile_documentation(content_dict):
    """Compile all scraped content into a single document"""
    # Sort URLs for consistent ordering
    sorted_urls = sorted(content_dict.keys())
    
    # Start with header
    doc = f"""# Claude Code Official Documentation

*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}*
*Scraped {len(content_dict)} pages from docs.anthropic.com*

---

## Table of Contents

"""
    # Add TOC
    for i, url in enumerate(sorted_urls, 1):
        title = content_dict[url]['title']
        anchor = re.sub(r'[^\w\s-]', '', title.lower()).replace(' ', '-')
        doc += f"{i}. [{title}](#{anchor})\n"
    
    doc += "\n---\n\n"
    
    # Add all content
    for url in sorted_urls:
        page = content_dict[url]
        doc += f"## {page['title']}\n\n"
        doc += f"*Source: {url}*\n\n"
        doc += page['content']
        doc += "\n\n---\n\n"
    
    return doc

if __name__ == "__main__":
    print("Starting comprehensive Claude Code documentation scrape...")
    all_content = scrape_claude_docs_recursive()
    
    if all_content:
        print(f"\nScraped {len(all_content)} pages successfully")
        documentation = compile_documentation(all_content)
        
        with open('official/docs.md', 'w', encoding='utf-8') as f:
            f.write(documentation)
        
        print("Documentation updated successfully")
    else:
        print("No content was scraped")
        # Write error message
        with open('official/docs.md', 'w', encoding='utf-8') as f:
            f.write(f"# Claude Code Official Documentation\n\n*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}*\n\nError: Unable to scrape documentation. The scraper may need updating.")
