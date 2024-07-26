import numpy as np
import validators
import requests
from requests.exceptions import SSLError, RequestException
from collections import Counter

def check_url(url):
    if not validators.url(url):
        return False

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return True
    except SSLError:
        try:
            response = requests.get(url, timeout=10, verify=False)
            if response.status_code == 200:
                return True
        except RequestException as e:
            print(f"Error fetching URL {url} after SSL failure: {e}")
    except RequestException as e:
        print(f"Error fetching URL {url}: {e}")

    return False

def get_final_prediction(ml_pred, llm_pred):
    data = [ml_pred]+llm_pred
    print(data)

    # Get predictions 
    predictions = [item['prediction'] for item in data]
    most_common_prediction = Counter(predictions).most_common(1)[0][0]

    # Finding the motivation associated with the highest probability
    llm_pred_filtered = [item for item in llm_pred if item['prediction'] == most_common_prediction]
    if llm_pred_filtered:
        max_proba_item = max(llm_pred_filtered, key=lambda x: x['proba'])
        max_motivation = max_proba_item.get('motivation', 'No motivation')
    else:
        max_motivation = 'No motivation'

    return {
        'prediction': "Legitimate" if most_common_prediction==0 else "Phishing",
        'proba': ml_pred['proba']*100,
        'motivation': max_motivation
    }