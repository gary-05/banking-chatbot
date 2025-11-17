
CRISIS_KEYWORDS = ["suicide", "kill myself", "end my life"]

def detect_crisis(text):
    for word in CRISIS_KEYWORDS:
        if word in text.lower():
            return True
    return False
