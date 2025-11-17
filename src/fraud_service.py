
import pickle
import numpy as np

class FraudDetector:
    def __init__(self, model_path="../models/iso_model.pkl"):
        try:
            with open(model_path, "rb") as f:
                self.model = pickle.load(f)
        except:
            self.model = None

    def extract_features(self, txn):
        return np.array([
            txn.get("amount", 0),
            txn.get("hour", 0),
            txn.get("daily_txn_count", 0)
        ]).reshape(1, -1)

    def predict_fraud(self, txn):
        if self.model is None:
            return {"fraud": False, "score": 0, "reason": "Model not loaded"}

        features = self.extract_features(txn)
        prediction = self.model.predict(features)[0]   # -1 = anomaly
        score = self.model.decision_function(features)[0]

        return {
            "fraud": prediction == -1,
            "score": float(score),
            "reason": "Anomaly detected" if prediction == -1 else "Normal"
        }
