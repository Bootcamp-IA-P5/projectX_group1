"""
Módulo de preprocesamiento de texto para modelos clásicos de ML.

Funciones:
- preprocess_for_tfidf: Pipeline completo (emojis, stopwords, lematización)
"""

import re
import emoji
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Inicializar recursos de NLTK
_stop_words = None
_lemmatizer = None


def _init_nltk():
    """Inicializa recursos de NLTK de forma lazy."""
    global _stop_words, _lemmatizer
    if _stop_words is None:
        _stop_words = set(stopwords.words('english'))
    if _lemmatizer is None:
        _lemmatizer = WordNetLemmatizer()


def preprocess_for_tfidf(text: str) -> str:
    """
    Preprocesamiento optimizado para TF-IDF:
    1. Convertir emojis a texto (😀 → grinning_face)
    2. Eliminar stopwords
    3. Lematizar
    
    Args:
        text: Texto original
        
    Returns:
        Texto preprocesado
    """
    _init_nltk()
    
    # 1. Convertir emojis a texto
    text = emoji.demojize(text, delimiters=(" ", " "))
    
    # 2. Tokenizar y procesar
    words = text.lower().split()
    
    # 3. Eliminar stopwords y lematizar
    processed_words = []
    for word in words:
        # Limpiar caracteres especiales
        word = re.sub(r'[^a-zA-Z_]', '', word)
        if word and word not in _stop_words:
            processed_words.append(_lemmatizer.lemmatize(word))
    
    return ' '.join(processed_words)
