from flask import Blueprint, render_template, redirect, request, jsonify
from utils.feature_extraction import extract_features

routes_bp = Blueprint('routes', __name__, url_prefix='/', template_folder='templates', static_folder='static')

@routes_bp.route('/')
def root():
    return redirect('/api/v1')

@routes_bp.route('/api/v1')
def index():
    return render_template('index.html')

@routes_bp.route('/api/v1/extract_features', methods=['POST'])
def extract_features_api():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    features = extract_features(url)
    if features is None:
        return jsonify({'error': 'Failed to extract features'}), 500
    
    return jsonify(features), 200

@routes_bp.route('/<path:dummy>')
def fallback(dummy):
    # Redirect when the path is incorrect 
    return redirect('/api/v1')