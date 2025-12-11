"""Script de prueba rápida del modelo LogisticRegression."""

import sys
import traceback
from pathlib import Path

# Agregar ruta de proyecto
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from backend.infer import predict_text

# Casos de prueba
test_cases = [
    "you are so stupid and dumb",
    "I hope you have a great day",
    "This is a very nice application, thank you!",
    "I hate you",
    "What a wonderful movie",
]

print("=" * 70)
print("PRUEBAS DE MODELO - LogisticRegression + TF-IDF")
print("=" * 70)

for text in test_cases:
    try:
        label, score = predict_text(text)
        print(f"\nTexto: '{text}'")
        print(f"  Etiqueta: {label.upper()} | Score: {score:.3f}")
    except Exception as e:
        print(f"\nError con '{text}': {e}")
        traceback.print_exc()

print("\n" + "=" * 70)
