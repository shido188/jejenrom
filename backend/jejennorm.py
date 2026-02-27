def normalize_text(text: str) -> str:
    """
    Simple Jejenorm (rule-based placeholder)
    You can improve this later with NLP/ML.
    """
    rules = {
        "u": "you",
        "ur": "your",
        "luv": "love",
        "c": "see",
        "r": "are",
        "2": "to",
        "4": "for"
    }

    words = text.lower().split()
    normalized_words = [rules.get(w, w) for w in words]
    return " ".join(normalized_words)