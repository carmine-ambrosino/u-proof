import re
import requests
from bs4 import BeautifulSoup
from joblib import load
import numpy as np
import pandas as pd
from flask import jsonify
from app.config import Config
from app.utils.utils import check_url

model = load(Config.ML_MODEL)

def predict_phishing(features):
    feature_names = [
        'IsHTTPS', 'HasPortNumber', 'HasDescription', 'HasSocialNet', 
        'HasFavicon', 'IsResponsive', 'HasTitle', 'HasHiddenFields'
    ]
    
    # Sort features according to the list of feature names
    feature_values = [features[name] for name in feature_names]
    
    # Create a DataFrame with the features
    feature_df = pd.DataFrame([feature_values], columns=feature_names)

    prediction = model.predict(feature_df)[0]
    prediction_proba = model.predict_proba(feature_df)[0]

    result = {
        'prediction': 0 if prediction == 0 else 1,
        'proba':  float(round(prediction_proba[0], 4)) if prediction == 0 else float(round(prediction_proba[1], 4))
    }

    return result

def extract_features(url):
    features = extract_url_features(url)
    html_features = extract_html_features(url)
    
    if html_features:
        features.update(html_features)
    
    return features

def extract_url_features(url):
    features = {}
    features['IsHTTPS'] = 1 if url.startswith('https') else 0
    features['HasPortNumber'] = 1 if re.search(r':[0-9]', url) else 0
    
    return features

def extract_html_features(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')

        features = {}
        features['HasDescription'] = check_description(soup)
        features['HasFavicon'] = check_favicon(soup)
        features['IsResponsive'] = check_responsive(soup)
        features['HasHiddenFields'] = check_hidden_fields(soup)
        features['HasTitle'] = check_title(soup)
        features['HasSocialNet'] = check_social_net(soup)
        
        return features

    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

def check_description(soup):
    description = soup.find('meta', attrs={'name': 'description'})
    return 1 if description else 0

def check_favicon(soup):
    favicon = soup.find('link', rel=lambda value: value and 'icon' in value)
    return 1 if favicon else 0

def check_responsive(soup):
    meta_tags = soup.find_all('meta', attrs={'name': 'viewport'})
    for tag in meta_tags:
        content = tag.get('content', '').lower()
        if 'width=device-width' in content and 'initial-scale=1.0' in content:
            return 1
    return 0

def check_hidden_fields(soup):
    hidden_fields = soup.find_all('input', type='hidden')
    return 1 if hidden_fields else 0

def check_title(soup):
    title = soup.find('title')
    return 1 if title else 0

def check_social_net(soup):
    social_keywords = ['twitter.com','facebook.com', 'linkedin.com', 'instagram.com', 'youtube.com', 'pinterest.com']
    links = soup.find_all('a', href=True)
    for link in links:
        if any(keyword in link['href'] for keyword in social_keywords):
            return 1

    # Check for social media meta tags (Open Graph, Twitter Cards)
    meta_tags = soup.find_all('meta')
    for tag in meta_tags:
        if tag.get('property') in ['og:site_name', 'og:title', 'og:description'] or \
           tag.get('name') in ['twitter:site', 'twitter:title', 'twitter:description']:
            return 1

    return 0

def get_ml_response(url):
    if check_url(url):
        features = extract_features(url)
        if features is None:
            return {'error': 'Failed to extract features'}, 500
        
        prediction_result = predict_phishing(features)

        # Combine features and prediction result
        response = {
            'url': url,
            **prediction_result
        }

        return response, 200
    else:
        return {'error': 'URL does not exist'}, 400