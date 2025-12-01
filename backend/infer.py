# Módulo de inferencia minimal: aquí cargaremos el modelo real.
# Ahora devuelve predicción "neutral" con score dummy.


def predict_text(text: str):
    """
    Predice etiqueta y score para un texto.
    Reemplaza esta función con la lógica real (cargar tokenizer/model y predecir).
    """
    # Ejemplo trivial: si aparece una palabra clave, devolver "toxic"
    toxic_keywords = ["odio", "asesinar", "matar", "idiota", "imbécil"]
    lower = text.lower()
    if any(k in lower for k in toxic_keywords):
        return "toxic", 0.85
    return "neutral", 0.12
