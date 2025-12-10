from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
# In Docker the working directory is /app (backend folder). Import locally.
from infer import predict_text
from pydantic import BaseModel

app = FastAPI(title="ProjectX - Hate Speech Detector (minimal backend)")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    if not payload.text or not payload.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    if len(payload.text) > 10000:
        raise HTTPException(status_code=400, detail="Text too long")
    try:
        label, score = predict_text(payload.text)
        return {
            "label": label,
            "score": score,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
