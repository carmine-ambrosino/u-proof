import re

def extract_features(url):
    features = {}
    features['length'] = len(url)
    features['is_https'] = int('https' in url)
    features['num_dashes'] = url.count('-')
    features['num_dots'] = url.count('.')
    return features