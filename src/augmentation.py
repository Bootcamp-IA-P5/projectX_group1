"""
Módulo de Data Augmentation para texto.

Técnicas disponibles:
- back_translation: Traduce a otro idioma y vuelve
- random_swap: Intercambia palabras aleatoriamente
- synonym_replacement: Reemplaza palabras por sinónimos (WordNet)
- augment_text: Aplica una técnica aleatoria
"""

import random
from typing import Callable, List

from deep_translator import GoogleTranslator
from nltk.corpus import wordnet


def back_translation(text: str, intermediate_lang: str = "es") -> str:
    """
    Traduce a otro idioma y vuelve para generar paráfrasis.

    Args:
        text: Texto original
        intermediate_lang: Idioma intermedio (default: español)

    Returns:
        Texto parafraseado
    """
    try:
        translated = GoogleTranslator(source="en", target=intermediate_lang).translate(
            text
        )
        back_translated = GoogleTranslator(
            source=intermediate_lang, target="en"
        ).translate(translated)
        return back_translated
    except Exception:
        return text  # Si falla, devuelve el original


def random_swap(text: str, n: int = 2) -> str:
    """
    Intercambia n pares de palabras aleatorias.

    Args:
        text: Texto original
        n: Número de intercambios

    Returns:
        Texto con palabras intercambiadas
    """
    words = text.split()
    if len(words) < 2:
        return text

    new_words = words.copy()
    for _ in range(n):
        idx1, idx2 = random.sample(range(len(new_words)), 2)
        new_words[idx1], new_words[idx2] = new_words[idx2], new_words[idx1]

    return " ".join(new_words)


def synonym_replacement(text: str, n: int = 2) -> str:
    """
    Reemplaza n palabras aleatorias por sinónimos usando WordNet.

    Args:
        text: Texto original
        n: Número de palabras a reemplazar

    Returns:
        Texto con sinónimos
    """
    words = text.split()
    if len(words) < 2:
        return text

    new_words = words.copy()
    word_indices = list(range(len(words)))
    random.shuffle(word_indices)

    replacements = 0
    for idx in word_indices:
        if replacements >= n:
            break
        word = words[idx]

        # Obtener sinónimos de WordNet
        synonyms = []
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                if lemma.name() != word and "_" not in lemma.name():
                    synonyms.append(lemma.name())

        if synonyms:
            new_words[idx] = random.choice(synonyms)
            replacements += 1

    return " ".join(new_words)


def augment_text(text: str, techniques: List[Callable] = None) -> str:
    """
    Aplica una técnica aleatoria de augmentation.

    Args:
        text: Texto original
        techniques: Lista de funciones de augmentation (default: todas)

    Returns:
        Texto aumentado
    """
    if techniques is None:
        techniques = [back_translation, random_swap, synonym_replacement]

    func = random.choice(techniques)
    return func(text)


def augment_dataset(
    texts: List[str], labels: List[int], n_augmentations: int = 2
) -> tuple:
    """
    Aumenta un dataset completo.

    Args:
        texts: Lista de textos originales
        labels: Lista de etiquetas
        n_augmentations: Número de versiones aumentadas por texto

    Returns:
        Tuple (textos_aumentados, labels_aumentados)
    """
    augmented_texts = []
    augmented_labels = []

    for text, label in zip(texts, labels):
        for _ in range(n_augmentations):
            augmented_texts.append(augment_text(text))
            augmented_labels.append(label)

    return augmented_texts, augmented_labels
