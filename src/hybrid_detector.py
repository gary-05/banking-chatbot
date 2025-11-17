
from rule_based import rule_based_checks
from fraud_service import FraudDetector

detector = FraudDetector()

def hybrid_check(txn):
    rule_hits = rule_based_checks(txn)
    ml_result = detector.predict_fraud(txn)

    return {
        "rule_based_alerts": rule_hits,
        "ml_alert": ml_result,
        "fraud": (len(rule_hits) > 0 or ml_result["fraud"])
    }
