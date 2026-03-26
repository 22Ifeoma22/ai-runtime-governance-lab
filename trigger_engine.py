trigger_engine.py
def evaluate_risk(score):
    if score >= 90:
        return "CRITICAL_STOP"
    elif score >= 70:
        return "ESCALATE"
    elif score >= 50:
        return "ALERT"
    return "NORMAL"
