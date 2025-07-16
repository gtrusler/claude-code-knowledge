import requests
from bs4 import BeautifulSoup

# Test if we can reach the docs
url = "https://docs.anthropic.com/en/docs/claude-code"
print(f"Testing URL: {url}")

try:
    response = requests.get(url, timeout=10, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    })
    print(f"Status code: {response.status_code}")
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Try to find navigation links
        links = soup.select('a[href*="/claude-code"]')
        print(f"Found {len(links)} Claude Code related links")
        
        # Print first 5 links
        for i, link in enumerate(links[:5]):
            href = link.get('href', '')
            text = link.get_text(strip=True)
            print(f"  {i+1}. {text} -> {href}")
            
except Exception as e:
    print(f"Error: {e}")
