
def rule_based_checks(txn):
    amount = txn.get("amount", 0)
    hour = txn.get("hour", 0)

    rules_triggered = []

    # Rule 1: Large amount
    if amount > 500000:
        rules_triggered.append("High transaction amount")

    # Rule 2: Odd time
    if hour < 5 or hour > 23:
        rules_triggered.append("Transaction at unusual hours")

    return rules_triggered
