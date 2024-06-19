from flask import Blueprint, render_template, redirect, request, jsonify
from utils.feature_extraction import extract_features, predict_phishing, check_url

routes_bp = Blueprint('routes', __name__, url_prefix='/', template_folder='templates', static_folder='static')

# ---- HOME ----
@routes_bp.route('/')
def root():
    return redirect('/api/v1')

@routes_bp.route('/api/v1')
def index():
    return render_template('index.html')
# ---------------

# ---- EXTRACT FEATURES ----
@routes_bp.route('/api/v1/extract_features', methods=['POST'])
def extract_features_api():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    url_exists = check_url(url)
    
    if url_exists:
        features = extract_features(url)
        if features is None:
            return jsonify({'error': 'Failed to extract features'}), 500
        
        prediction_result = predict_phishing(features)

        # Combine features and prediction result
        response = {
            'features': features,
            **prediction_result
        }

        return jsonify(response), 200
    else:
        return jsonify({'error': 'URL {url} does not exist'}), 400

# ---------------


# ---- URL ANALYSIS ----
@routes_bp.route('/api/v1/url')
def analysis():
    return render_template('analysis.html')
# ---------------


# ---- PATH ERROR ----
@routes_bp.route('/<path:dummy>')
def fallback(dummy):
    # Redirect when the path is incorrect 
    return redirect('/api/v1')
# ---------------