from typing import Any, Dict

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI(title="ProjectX - Hate Speech Detector")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "ProjectX Hate Speech Detector API", "status": "running"}


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/predict")
async def predict(payload: Dict[str, Any]):
    text = payload.get("text", "")

    if not text or not text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    if len(text) > 10000:
        raise HTTPException(
            status_code=400, detail="Text too long (max 10000 characters)"
        )

    # Simple keyword-based classifier (fallback)
    hate_keywords = [
        "odio",
        "idiota",
        "estúpido",
        "tonto",
        "imbécil",
        "pendejo",
        "mierda",
        "hate",
        "stupid",
        "idiot",
        "dumb",
        "moron",
        "trash",
        "garbage",
    ]

    text_lower = text.lower()
    has_hate_words = any(keyword in text_lower for keyword in hate_keywords)

    if has_hate_words:
        label = "toxic"
        score = 0.75
    else:
        label = "safe"
        score = 0.85

    return {
        "label": label,
        "score": score,
        "prediction": label,
        "confidence": score,
        "probabilities": {label: score, "other": 1 - score},
        "text_length": len(text),
        "model": "fallback_keyword_classifier",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
