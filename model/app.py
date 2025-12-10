from fastapi import FastAPI
from pydantic import BaseModel

# Aquí puedes cargar tu modelo real (transformers/torch) al inicio.
# Por ahora devolvemos respuesta dummy para integración.


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    label: str
    score: float


app = FastAPI(title="Model Server - ProjectX")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionOut)
async def predict(payload: TextIn):
    text = payload.text.lower()
    toxic_keywords = ["odio", "matar", "asesinar", "idiota", "imbécil"]
    if any(k in text for k in toxic_keywords):
        return {"label": "toxic", "score": 0.9}
    return {"label": "neutral", "score": 0.1}
