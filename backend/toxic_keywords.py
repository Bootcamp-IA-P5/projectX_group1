"""
Toxic Keywords Configuration
Enhanced hate speech detection patterns with toxicity weights
"""

# Spanish toxic patterns (regex patterns with toxicity weights 0.0-1.0)
SPANISH_TOXIC_PATTERNS = {
    # Very high toxicity (0.9-1.0)
    r"\b(imbecil|imbécil|careculo|cabrón|cabron)\b": 0.95,
    r"\b(puto|puta|hijo de puta|hdp|hijo de su madre)\b": 0.98,
    r"\b(maldito|desgraciado|miserable|rata)\b": 0.92,
    # High toxicity (0.8-0.9)
    r"\b(idiota|estupido|estúpido|pendejo|tarado)\b": 0.88,
    r"\b(mierda|carajo|coño|joder)\b": 0.85,
    r"\b(matar|morir|muerte|odio|odiar)\b": 0.87,
    r"\b(basura|escoria|inmundo|asqueroso)\b": 0.83,
    # Medium toxicity (0.6-0.8)
    r"\b(tonto|bobo|bruto|animal|bestia)\b": 0.72,
    r"\b(inutil|inútil|mediocre|fracasado)\b": 0.68,
    r"\b(gordo|feo|horrible|fea)\b": 0.65,
}

# English toxic patterns
ENGLISH_TOXIC_PATTERNS = {
    # Very high toxicity (0.9-1.0)
    r"\b(fuck|fucking|motherfucker|asshole|bitch)\b": 0.96,
    r"\b(shit|crap|damn|bastard|dick)\b": 0.90,
    # High toxicity (0.8-0.9)
    r"\b(idiot|stupid|dumb|moron|retard)\b": 0.88,
    r"\b(hate|kill|die|death|murder)\b": 0.92,
    r"\b(trash|garbage|scum|filth)\b": 0.84,
    # Medium toxicity (0.6-0.8)
    r"\b(loser|pathetic|worthless|useless)\b": 0.75,
    r"\b(ugly|fat|horrible|disgusting)\b": 0.68,
}

# Combine all patterns
ALL_TOXIC_PATTERNS = {**SPANISH_TOXIC_PATTERNS, **ENGLISH_TOXIC_PATTERNS}

# Safe context patterns (reduce toxicity when detected)
SAFE_CONTEXT_PATTERNS = [
    r"\b(no soy|no eres|no es|not a|not an)\b.*\b(idiota|tonto|estúpido|idiot|stupid)\b",
    r"\b(amigo|friend|brother|hermano|bro|buddy)\b",
    r"\b(jok(e|ing)|broma|chiste)\b",  # Joking context
]

# Toxicity thresholds
TOXICITY_THRESHOLD = 0.6  # Above this = toxic
SAFE_CONTEXT_REDUCTION = 0.5  # Multiply toxicity by this when safe context detected
MULTIPLE_MATCHES_BONUS = 0.1  # Add this when multiple toxic words found
