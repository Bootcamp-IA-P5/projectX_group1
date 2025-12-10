import os
from typing import Tuple

import requests

MODEL_URL = os.environ.get("MODEL_URL", "http://model:8001")


def predict_text(text: str) -> Tuple[str, float]:
    """
    Llama al model-server para obtener la predicción.
    Si el model-server no está disponible, puedes manejar fallback local.
    """
    try:
        resp = requests.post(f"{MODEL_URL}/predict", json={"text": text}, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        # data expected: {"label": "...", "score": 0.12}
        return data.get("label", "error"), float(data.get("score", 0.0))
    except Exception as e:
        # Fallback: análisis simple basado en palabras clave
        print(f"Model server error: {e}. Using fallback prediction.")

        # Lista simple de palabras de odio (expandir según necesidad)
        hate_keywords = [
            "odio",
            "idiota",
            "estúpido",
            "tonto",
            "hate",
            "stupid",
            "idiot",
            "dumb",
        ]

        text_lower = text.lower()
        has_hate_words = any(keyword in text_lower for keyword in hate_keywords)

        if has_hate_words:
            return "toxic", 0.75
        else:
            return "safe", 0.85
