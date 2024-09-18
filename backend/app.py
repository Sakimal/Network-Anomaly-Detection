from flask import Flask, request, jsonify
import joblib
from prometheus_client import start_http_server, Summary

app = Flask(__name__)

# Prometheus metrics
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Load the pre-trained Isolation Forest model
model = joblib.load('model.joblib')

@app.route('/predict', methods=['POST'])
@REQUEST_TIME.time()
def predict():
    data = request.json
    features = data['features']  # The packet data needs to be formatted as the model's input
    prediction = model.predict([features])
    return jsonify({'prediction': 'anomaly' if prediction[0] == -1 else 'normal'})

if __name__ == '__main__':
    # Start Prometheus metrics server on port 8000
    start_http_server(8000)
    app.run(debug=True, host='0.0.0.0', port=5000)
