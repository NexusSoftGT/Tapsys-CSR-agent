import re

# 🧠 Your domain knowledge base
ISSUE_KB = [
    {
        "issue_id": "batch_settlement",
        "keywords": ["batch", "settle", "clear"],
        "clarify": "Kya aap ka POS batch settle nahi ho raha?",
        "guide": "Aap ke POS terminal pe 'Clear Batch' ka button hoga, usay press karein."
    },
    {
        "issue_id": "missing_payment",
        "keywords": ["payment", "paisay", "account", "transaction", "nahi aayi", "paisa"],
        "clarify": "Kya aap ko kisi transaction ki payment nahi mili?",
        "guide": "Kis tareekh ki transaction ka paisa nahi aaya? Ham check kar ke aap ko update dein ge."
    },
    {
        "issue_id": "paper_roll",
        "keywords": ["roll", "paper", "print", "khatam", "slip"],
        "clarify": "Kya aap ke paas Paper roll khatam hogaye hain?",
        "guide": "Aap ka paper roll khatam hogaya hai. Naya roll insert karein, agar masla jari raha to humein contact karein."
    },
    {
        "issue_id": "battery_issue",
        "keywords": ["battery", "charge", "charging", "power", "off", "band"],
        "clarify": "Kya aap ki POS device charge nahi ho rahi?",
        "guide": "Please charger check karein aur ensure karein ke device sahi tarah se plug in hai."
    },
    {
        "issue_id": "pos_error",
        "keywords": ["error", "screen", "message", "device", "masla", "issue"],
        "clarify": "Kya aap mujhe screen pe likha error read karke bata sakte hain?",
        "guide": "Agar screen pe error aa raha hai to device ko restart karein ya support se rabta karein."
    }
]

def search_rag(transcript):
    """Search KB to find matching issue from transcript"""
    transcript = transcript.lower()

    for issue in ISSUE_KB:
        if any(re.search(rf"\b{keyword}\b", transcript) for keyword in issue["keywords"]):
            return {
                "issue_id": issue["issue_id"],
                "clarify": issue["clarify"],
                "guide": issue["guide"]
            }

    return None


CONFIRM_KEYWORDS = ["haan", "yes", "jee", "bilkul", "sahi", "ji", "theek"]

def confirm_intent(response):
    """Check if user's response is a confirmation"""
    response = response.lower()
    return any(re.search(rf"\b{word}\b", response) for word in CONFIRM_KEYWORDS)
