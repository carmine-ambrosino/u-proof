from flask import render_template, request, jsonify
from . import api_v1_bp

from app.config import Config

from app.utils.ml_utils import get_ml_response
from app.utils.llm_utils import get_llm_response
from app.utils.utils import get_final_prediction

@api_v1_bp.route('/')
def index():
    return render_template('index.html')

@api_v1_bp.route('/predict', methods=['POST'])
def predict_api():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    ml_response, status_code = get_ml_response(url)

    llm_response = get_llm_response(Config.PROMPT.replace("[url_here]", url), Config.MODELS)
    
    prediction = get_final_prediction(ml_response, llm_response)
    prediction["url"] = url

    return jsonify(prediction)


@api_v1_bp.route('/result')
def result():
    return render_template('analysis.html')