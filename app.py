from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return "🚀 ML Anomaly Detection API is Live"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array([[data['packet_rate'], data['connection_count'], data['ip_entropy']]])
    prediction = model.predict(features)[0]
    return jsonify({'is_anomalous': bool(prediction)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
