from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from backend.infer import predict_text

app = FastAPI(title="ProjectX - Hate Speech Detector (minimal backend)")


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    label: str
    score: float


@app.get("/")
async def root():
    # Redirige a la documentación interactiva
    return RedirectResponse(url="/docs")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionOut)
async def predict(payload: TextIn):
    # predict_text debe devolver (label, score)
    label, score = predict_text(payload.text)
    return {"label": label, "score": score}
