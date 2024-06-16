from flask import Flask, request, jsonify, render_template
from utils.feature_extraction import extract_features

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/extract_features', methods=['POST'])
def extract_features_api():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    features = extract_features(url)
    if features is None:
        return jsonify({'error': 'Failed to extract features'}), 500
    
    return jsonify(features), 200



if __name__ == '__main__':
    app.run(debug=True)