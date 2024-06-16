from flask import Flask, request, jsonify, render_template
from utils.feature_extraction import extract_features

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/extract_features', methods=['POST'])
def extract_features_api():
    request_data = request.get_json()

    if 'url' not in request_data:
        return jsonify({'error': 'URL not found in JSON request'}), 400

    url = request_data['url']
    features = extract_features(url)
    return jsonify(features), 200



if __name__ == '__main__':
    app.run(debug=True)