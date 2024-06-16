import re
import requests
from bs4 import BeautifulSoup

def extract_features(url):
    features = extract_url_features(url)
    html_features = extract_html_features(url)
    
    if html_features:
        features.update(html_features)
    
    return features

def extract_url_features(url):
    """
    Extracts features directly from the URL.
    """
    features = {}
    features['is_https'] = 1 if url.startswith('https') else 0
    features['has_port_number'] = 1 if re.search(r':[0-9]', url) else 0

    letters_count = sum(c.isalpha() for c in url)
    features['url_letter_ratio'] = letters_count / len(url) if len(url) > 0 else 0.0

    special_chars_count = len(re.findall(r'[^a-zA-Z0-9]', url))
    features['url_special_char_ratio'] = special_chars_count / len(url) if len(url) > 0 else 0.0

    # features['letter_count'] = letters_count
    # features['special_chars_count'] = special_chars_count
    # features['url_length'] = len(url)
    # features['num_dashes'] = url.count('-')
    # features['num_dots'] = url.count('.')

    return features

def extract_html_features(url):
    """
    Extracts features from the HTML content of the page.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')

        features = {}
        features['has_description'] = check_description(soup)
        features['has_favicon'] = check_favicon(soup)
        features['is_responsive'] = check_responsive(soup)
        features['has_hidden_fields'] = check_hidden_fields(soup)
        
        return features

    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

def check_description(soup):
    """
    Checks if the page has a meta description tag.
    """
    description = soup.find('meta', attrs={'name': 'description'})
    return 1 if description else 0

def check_favicon(soup):
    """
    Checks if the page has a favicon.
    """
    favicon = soup.find('link', rel=lambda value: value and 'icon' in value)
    return 1 if favicon else 0

def check_responsive(soup):
    """
    Checks if the page is responsive.
    """
    meta_tags = soup.find_all('meta', attrs={'name': 'viewport'})
    for tag in meta_tags:
        content = tag.get('content', '').lower()
        if 'width=device-width' in content and 'initial-scale=1.0' in content:
            return 1
    return 0

def check_hidden_fields(soup):
    """
    Checks if the page has hidden input fields.
    """
    hidden_fields = soup.find_all('input', type='hidden')
    return 1 if hidden_fields else 0