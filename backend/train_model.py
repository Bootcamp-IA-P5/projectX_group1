"""
Script para entrenar un modelo LogisticRegression básico desde cero.
Usa los datasets que ya tenemos.
"""

import sys
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Agregar ruta de proyecto
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.preprocessing import preprocess_for_tfidf

print("=" * 70)
print("ENTRENAR MODELO LOGISTIC REGRESSION + TF-IDF")
print("=" * 70)

# Cargar datos
data_file = PROJECT_ROOT / "data" / "processed" / "youtoxic_english_1000.csv"
print(f"\n1. Cargando datos desde: {data_file}")

df = pd.read_csv(data_file)
print(f"   Total registros: {len(df)}")
print(f"   Columnas: {list(df.columns)}")

# Usar columna IsToxic como etiqueta
X = df["Text"].values
y = df["IsToxic"].values

print(f"   Distribución de clases: {np.bincount(y)}")

# Split train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\n2. Train/Test split:")
print(f"   Train: {len(X_train)}")
print(f"   Test: {len(X_test)}")

# Preprocesar
print(f"\n3. Preprocesando textos...")
X_train_processed = [preprocess_for_tfidf(text) for text in X_train]
X_test_processed = [preprocess_for_tfidf(text) for text in X_test]

# TF-IDF
print(f"\n4. Vectorizando con TF-IDF...")
vectorizer = TfidfVectorizer(
    max_features=250,
    min_df=2,
    max_df=0.95,
    ngram_range=(1, 2),  # Usar unigramas y bigramas
    lowercase=True,
    stop_words="english",
)
X_train_tfidf = vectorizer.fit_transform(X_train_processed)
X_test_tfidf = vectorizer.transform(X_test_processed)

print(f"   Features: {X_train_tfidf.shape[1]}")

# Entrenar modelo con hiperparámetros mejorados
print(f"\n5. Entrenando LogisticRegression...")
model = LogisticRegression(
    C=0.1,  # Regularización más débil para mejor fit
    max_iter=1000,
    random_state=42,
    class_weight="balanced",  # Manejar desbalance de clases
)
model.fit(X_train_tfidf, y_train)

# Evaluar
train_score = model.score(X_train_tfidf, y_train)
test_score = model.score(X_test_tfidf, y_test)

print(f"   Train Accuracy: {train_score:.4f}")
print(f"   Test Accuracy: {test_score:.4f}")

# Guardar modelo
models_dir = PROJECT_ROOT / "models"
models_dir.mkdir(exist_ok=True)

model_path = models_dir / "logreg_C0.0001_feat250_aug5.joblib"
vectorizer_path = models_dir / "logreg_C0.0001_feat250_aug5_vectorizer.joblib"

joblib.dump(model, model_path)
joblib.dump(vectorizer, vectorizer_path)

print(f"\n6. Modelo guardado:")
print(f"   {model_path}")
print(f"   {vectorizer_path}")

print("\n" + "=" * 70)
print("✓ ENTRENAMIENTO COMPLETADO")
print("=" * 70)
