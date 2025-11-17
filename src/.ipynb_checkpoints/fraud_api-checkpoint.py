
from flask import Flask, request, jsonify
from fraud_service import FraudDetector

app = Flask(__name__)
detector = FraudDetector()

@app.route("/fraud-check", methods=["POST"])
def fraud_check():
    data = request.json
    result = detector.predict_fraud(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
