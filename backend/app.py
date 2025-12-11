"""
FastAPI backend para hate speech detection.
Todo en un solo archivo para evitar problemas de imports en Docker.
"""

import re
from pathlib import Path
from typing import Tuple

import joblib
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

# ===== PREPROCESSING INLINE =====
try:
    import emoji
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer

    HAS_NLTK = True
except:
    HAS_NLTK = False

_stop_words = None
_lemmatizer = None


def _init_nltk():
    """Inicializa NLTK resources."""
    global _stop_words, _lemmatizer
    if not HAS_NLTK:
        return
    try:
        _stop_words = set(stopwords.words("english"))
        _lemmatizer = WordNetLemmatizer()
    except:
        try:
            import nltk

            nltk.download("stopwords", quiet=True)
            nltk.download("wordnet", quiet=True)
            _stop_words = set(stopwords.words("english"))
            _lemmatizer = WordNetLemmatizer()
        except:
            pass


def preprocess_for_tfidf(text: str) -> str:
    """Preprocesamiento para TF-IDF."""
    if not HAS_NLTK:
        return text.lower()

    _init_nltk()

    if _stop_words is None or _lemmatizer is None:
        return text.lower()

    try:
        text = emoji.demojize(text, delimiters=(" ", " "))
    except:
        pass

    words = text.lower().split()
    processed_words = []

    for word in words:
        word = re.sub(r"[^a-zA-Z_]", "", word)
        if word and word not in _stop_words:
            processed_words.append(_lemmatizer.lemmatize(word))

    return " ".join(processed_words)


# ===== MODEL LOADING =====
APP_DIR = Path(__file__).parent
MODEL_PATH = APP_DIR.parent / "models" / "logreg_C0.0001_feat250_aug5.joblib"
VECTORIZER_PATH = (
    APP_DIR.parent / "models" / "logreg_C0.0001_feat250_aug5_vectorizer.joblib"
)

_model = None
_vectorizer = None


def _load_model():
    """Carga el modelo y vectorizador."""
    global _model, _vectorizer

    if _model is None:
        if not MODEL_PATH.exists() or not VECTORIZER_PATH.exists():
            print(f"⚠ Modelos no encontrados en {MODEL_PATH}")
            raise FileNotFoundError(f"Modelos no encontrados")

        _model = joblib.load(MODEL_PATH)
        _vectorizer = joblib.load(VECTORIZER_PATH)
        print(f"✓ Modelo cargado")

    return _model, _vectorizer


def predict_text(text: str) -> Tuple[str, float]:
    """Predice etiqueta y score."""
    try:
        model, vectorizer = _load_model()
        preprocessed = preprocess_for_tfidf(text)
        features = vectorizer.transform([preprocessed])
        proba = model.predict_proba(features)[0]
        toxic_score = float(proba[1])
        label = "toxic" if toxic_score >= 0.5 else "safe"
        return label, toxic_score
    except Exception as e:
        print(f"Error en predicción: {e}")
        return "safe", 0.5


# ===== FASTAPI APP =====
app = FastAPI(title="ProjectX - Hate Speech Detector")

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
