import re
from typing import Dict, List

from fastapi import FastAPI
from pydantic import BaseModel


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    label: str
    score: float


app = FastAPI(title="Model Server - ProjectX")


# Keyword-based heuristic model with context adjustments.
SPANISH_TOXIC_PATTERNS: Dict[str, float] = {
    r"\b(imbecil|imbécil|careculo|cabrón|cabron)\b": 0.95,
    r"\b(puto|puta|hijo de puta|hdp|hijo de su madre)\b": 0.98,
    r"\b(maldito|desgraciado|miserable|rata)\b": 0.92,
    r"\b(idiota|estupido|estúpido|pendejo|tarado)\b": 0.88,
    r"\b(mierda|carajo|coño|joder)\b": 0.85,
    r"\b(matar|morir|muerte|odio|odiar)\b": 0.87,
    r"\b(basura|escoria|inmundo|asqueroso)\b": 0.83,
    r"\b(tonto|bobo|bruto|animal|bestia)\b": 0.72,
    r"\b(inutil|inútil|mediocre|fracasado)\b": 0.68,
    r"\b(gordo|feo|horrible|fea)\b": 0.65,
}

ENGLISH_TOXIC_PATTERNS: Dict[str, float] = {
    r"\b(fuck|fucking|motherfucker|asshole|bitch)\b": 0.96,
    r"\b(shit|crap|damn|bastard|dick)\b": 0.90,
    r"\b(idiot|stupid|dumb|moron|retard)\b": 0.88,
    r"\b(hate|kill|die|death|murder)\b": 0.92,
    r"\b(trash|garbage|scum|filth)\b": 0.84,
    r"\b(loser|pathetic|worthless|useless)\b": 0.75,
    r"\b(ugly|fat|horrible|disgusting)\b": 0.68,
}

ALL_TOXIC_PATTERNS: Dict[str, float] = {**SPANISH_TOXIC_PATTERNS, **ENGLISH_TOXIC_PATTERNS}

SAFE_CONTEXT_PATTERNS: List[str] = [
    r"\b(no soy|no eres|no es|not a|not an)\b.*\b(idiota|tonto|estúpido|idiot|stupid)\b",
    r"\b(amigo|friend|brother|hermano|bro|buddy)\b",
    r"\b(jok(e|ing)|broma|chiste)\b",
    # Af fection / cariño lower toxicity when present
    r"\b(te amo|te quiero|amor|cariño|mi vida|mi amor|querido|precioso|hermos(o|a))\b",
]

SAFE_CONTEXT_REDUCTION = 0.5
POSITIVE_CONTEXT_REDUCTION = 0.35
MULTIPLE_MATCHES_BONUS = 0.12
TOXICITY_THRESHOLD = 0.65


@app.get("/health")
async def health():
    return {"status": "ok"}


def _compute_score(text: str) -> Dict[str, float]:
    text_lower = text.lower()
    matched_weights: List[float] = []
    matched_patterns: List[str] = []

    for pattern, weight in ALL_TOXIC_PATTERNS.items():
        if re.search(pattern, text_lower, re.IGNORECASE):
            matched_weights.append(weight)
            matched_patterns.append(pattern)

    if not matched_weights:
        return {
            "label": "safe",
            "score": 0.1,
            "matches": matched_patterns,
            "safe_context": False,
        }

    base_score = max(matched_weights)

    # Multiple toxic cues slightly increase certainty
    if len(matched_weights) > 1:
        base_score = min(0.99, base_score + MULTIPLE_MATCHES_BONUS)

    has_safe_context = any(
        re.search(ctx, text_lower, re.IGNORECASE) for ctx in SAFE_CONTEXT_PATTERNS
    )

    adjusted_score = base_score
    if has_safe_context:
        adjusted_score *= SAFE_CONTEXT_REDUCTION
    # Extra reduction for positive/affectionate wording so one insult in a loving
    # sentence does not dominate the prediction completely.
    if has_safe_context:
        adjusted_score *= 1 - POSITIVE_CONTEXT_REDUCTION

    adjusted_score = max(0.0, min(0.99, adjusted_score))

    label = "toxic" if adjusted_score >= TOXICITY_THRESHOLD else "safe"
    return {
        "label": label,
        "score": round(adjusted_score, 4),
        "matches": matched_patterns,
        "safe_context": has_safe_context,
    }


@app.post("/predict", response_model=PredictionOut)
async def predict(payload: TextIn):
    result = _compute_score(payload.text)
    return PredictionOut(label=result["label"], score=result["score"])
