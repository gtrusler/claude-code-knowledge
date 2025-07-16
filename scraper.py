import requests
from bs4 import BeautifulSoup
import markdownify
from datetime import datetime
import time
import os

def extract_page_links(soup):
    """Extract all Claude Code links from a page"""
    links = set()
    
    # Find all links containing /claude-code
    for link in soup.find_all('a', href=True):
        href = link['href']
        if '/claude-code' in href:
            # Convert relative to absolute
            if href.startswith('/'):
                href = f"https://docs.anthropic.com{href}"
            # Remove fragments and query params
            href = href.split('#')[0].split('?')[0]
            links.add(href)
    
    return links

def scrape_page(url, max_retries=3):
    """Scrape a single page with retries"""
    for attempt in range(max_retries):
        try:
            print(f"  Attempt {attempt + 1} for {url}")
            response = requests.get(url, timeout=15, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            })
            
            if response.status_code != 200:
                print(f"  Got status {response.status_code}")
                continue
                
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find main content
            content = (
                soup.find('main') or 
                soup.find('article') or 
                soup.find('div', {'class': 'content'}) or
                soup.find('div', {'role': 'main'})
            )
            
            if not content:
                print(f"  No content found")
                return None, set()
            
            # Convert to markdown
            markdown = markdownify.markdownify(str(content), heading_style="ATX")
            
            # Get links from this page
            links = extract_page_links(soup)
            
            return markdown, links
            
        except Exception as e:
            print(f"  Error on attempt {attempt + 1}: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)  # Wait before retry
    
    return None, set()

def scrape_claude_docs():
    """Scrape all Claude Code documentation"""
    base_url = "https://docs.anthropic.com/en/docs/claude-code"
    
    print("Starting Claude Code documentation scrape...")
    
    # Track what we've visited
    visited = set()
    to_visit = {base_url}
    
    # Known pages to ensure we get
    known_pages = [
        'overview', 'quickstart', 'getting-started', 'setup',
        'cli-reference', 'slash-commands', 'interactive-mode',
        'common-workflows', 'settings', 'memory',
        'hooks', 'mcp', 'sdk', 'github-actions',
        'ide-integrations', 'troubleshooting',
        'amazon-bedrock', 'google-vertex-ai', 'bedrock-vertex'
    ]
    
    for page in known_pages:
        to_visit.add(f"{base_url}/{page}")
    
    # Collect all content
    pages = {}
    
    while to_visit:
        url = to_visit.pop()
        
        # Skip if visited or not claude-code
        if url in visited or '/claude-code' not in url:
            continue
            
        visited.add(url)
        print(f"\nScraping: {url}")
        
        # Wait between requests
        time.sleep(1)
        
        # Scrape the page
        content, links = scrape_page(url)
        
        if content:
            # Store the content
            page_name = url.split('/')[-1] or 'overview'
            pages[page_name] = {
                'url': url,
                'content': content
            }
            print(f"  Success! Found {len(links)} links")
            
            # Add new links to visit
            for link in links:
                if link not in visited:
                    to_visit.add(link)
        else:
            print(f"  Failed to scrape")
    
    # Build the final document
    print(f"\nBuilding final document from {len(pages)} pages...")
    
    doc_parts = []
    
    # Header
    doc_parts.append(f"""# Claude Code Official Documentation

*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}*
*Source: {base_url}*

This documentation is automatically scraped from Anthropic's official docs.

---

## Table of Contents

""")
    
    # Sort pages for consistent ordering
    sorted_pages = sorted(pages.items())
    
    # Add TOC
    for page_name, page_data in sorted_pages:
        title = page_name.replace('-', ' ').title()
        doc_parts.append(f"- [{title}](#{page_name})\n")
    
    # Add content
    for page_name, page_data in sorted_pages:
        title = page_name.replace('-', ' ').title()
        doc_parts.append(f"\n\n---\n\n## {title}\n\n")
        doc_parts.append(f"*Source: {page_data['url']}*\n\n")
        doc_parts.append(page_data['content'])
    
    return ''.join(doc_parts)

if __name__ == "__main__":
    # Ensure output directory exists
    os.makedirs('official', exist_ok=True)
    
    # Scrape the docs
    docs_content = scrape_claude_docs()
    
    # Write to file
    output_path = 'official/docs.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(docs_content)
    
    print(f"\n✅ Documentation updated successfully!")
    print(f"📄 Wrote {len(docs_content):,} characters to {output_path}")
    print(f"📑 Total pages scraped: {docs_content.count('---') - 1}")
