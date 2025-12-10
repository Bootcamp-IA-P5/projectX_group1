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
        # Fallback sencillo (mantén comportamiento seguro)
        print("Model server error:", e)
        return "neutral", 0.0
