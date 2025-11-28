# -*- coding: utf-8 -*-
"""
scripts/wordcloud_lengths.py
Script para:
 - Cargar un CSV con textos (columna especificada por --text-col)
 - Limpiar y preprocesar (lemmatizar con spaCy)
 - Generar WordClouds y gráficos de longitud
 - Exportar top-k palabras

Uso:
 python scripts/wordcloud_lengths.py --input data/processed/youtoxic_english_1000.csv --text-col Text --output outputs_youtoxic --sample-frac 0.05 --lang en

Comentarios:
 - El script detecta el idioma con --lang (en o es). En inglés cargará en_core_web_sm.
 - Si falta stopwords de NLTK, el script intentará descargarlas (requiere internet la primera vez).
"""
import argparse
import os
import re
from collections import Counter

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

import spacy
import nltk
from nltk.corpus import stopwords

# ---------------------------
# Helpers y carga de recursos
# ---------------------------

def ensure_nltk_resources(lang="english"):
    """
    Asegura que las stopwords de NLTK estén descargadas.
    Se ejecuta la primera vez que uses el script.
    """
    # Determina el idioma de stopwords según el parámetro lang
    language = "spanish" if str(lang).lower().startswith("es") else "english"
    try:
        stopwords.words(language)
    except LookupError:
        print(f"Descargando recursos NLTK (stopwords para {language})...")
        nltk.download('stopwords')
        nltk.download('punkt')

def load_spacy_model(lang):
    """
    Carga un modelo spaCy según el idioma solicitado.
    - 'en' -> en_core_web_sm
    - 'es' -> es_core_news_sm
    Si el modelo no está instalado, imprime la instrucción para instalarlo y levanta error.
    """
    if lang.startswith("en"):
        model_name = "en_core_web_sm"
    elif lang.startswith("es"):
        model_name = "es_core_news_sm"
    else:
        raise ValueError("Idioma no soportado: usa 'en' o 'es'")

    try:
        nlp = spacy.load(model_name)
        return nlp
    except OSError as e:
        raise OSError(f"El modelo spaCy '{model_name}' no está instalado. Instálalo con:\npython -m spacy download {model_name}") from e

# ---------------------------
# Preprocesado de texto
# ---------------------------

def get_stopwords_for_lang(lang):
    """
    Devuelve un set de stopwords para el idioma seleccionado (NLTK).
    Añade tokens extra comunes.
    """
    ensure_nltk_resources(lang)
    if lang.startswith("en"):
        sw = set(stopwords.words("english"))
        extra = {"rt", "https", "http", "amp", "u", "im", "dont", "cant"}
    else:
        sw = set(stopwords.words("spanish"))
        extra = {"rt", "https", "http", "amp", "q", "u"}
    sw |= extra
    return sw

def clean_text(text, nlp, stopwords_set):
    """
    Limpia y lematiza texto:
    - minúsculas, eliminar URLs, menciones y hashtags
    - quitar caracteres no alfanuméricos (mantener espacios y letras acentuadas)
    - tokenizar y lematizar con spaCy
    - filtrar stopwords y tokens vacíos
    Devuelve string lematizado.
    """
    if pd.isna(text):
        return ""
    text = str(text)
    # Normalizar y eliminar URLs, menciones
    text = text.lower()
    text = re.sub(r'http\S+|www\.\S+', '', text)
    text = re.sub(r'@\w+|#\w+', '', text)
    # Reemplazar caracteres no alfabéticos (conservamos letras acentuadas y números si quieres)
    text = re.sub(r'[^a-záéíóúüñ0-9\s]', ' ', text)
    # Tokenizar y lematizar
    doc = nlp(text)
    lemmas = []
    for token in doc:
        if token.is_space or token.is_punct:
            continue
        lemma = token.lemma_.strip()
        if not lemma:
            continue
        # Filtrar stopwords y tokens muy cortos
        if lemma in stopwords_set or len(lemma) <= 1:
            continue
        lemmas.append(lemma)
    return " ".join(lemmas)

# ---------------------------
# Visualizaciones / Export
# ---------------------------

def generate_wordcloud(text_series, output_path, max_words=200, background_color="white"):
    """
    Genera y guarda una wordcloud a partir de una Serie de pandas con textos limpios.
    """
    full_text = " ".join(text_series.dropna().astype(str).values)
    if not full_text.strip():
        print("No hay texto para generar wordcloud.")
        return
    wc = WordCloud(width=1600, height=800, background_color=background_color,
                   max_words=max_words, collocations=False, colormap="viridis")
    wc.generate(full_text)
    wc.to_file(output_path)
    print(f"Wordcloud guardada en {output_path}")

def plot_length_distributions(lengths, output_path_hist, output_path_box):
    """
    Dibuja histograma y boxplot de longitudes (en tokens) y guarda las figuras.
    """
    if lengths.size == 0:
        print("No hay longitudes para graficar.")
        return
    plt.figure(figsize=(10, 6))
    sns.histplot(lengths, bins=50, kde=True)
    plt.title("Distribución de longitudes de texto (tokens)")
    plt.xlabel("Número de tokens")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.savefig(output_path_hist, dpi=150)
    plt.close()

    plt.figure(figsize=(8, 4))
    sns.boxplot(x=lengths)
    plt.title("Boxplot de longitudes de texto (tokens)")
    plt.xlabel("Número de tokens")
    plt.tight_layout()
    plt.savefig(output_path_box, dpi=150)
    plt.close()

# ---------------------------
# Main
# ---------------------------

def main(args):
    # Leer CSV
    df = pd.read_csv(args.input)
    if args.text_col not in df.columns:
        raise ValueError(f"La columna '{args.text_col}' no está en el CSV. Columnas disponibles: {df.columns.tolist()}")

    # Cargar modelo spaCy según idioma
    nlp = load_spacy_model(args.lang)
    stopwords_set = get_stopwords_for_lang(args.lang)

    # Crear carpetas de salida
    os.makedirs(args.output, exist_ok=True)
    os.makedirs(os.path.join(args.output, "wordclouds"), exist_ok=True)
    os.makedirs(os.path.join(args.output, "plots"), exist_ok=True)

    # Muestra opcional
    if args.sample_frac and 0 < args.sample_frac < 1:
        df = df.sample(frac=args.sample_frac, random_state=42)
        print(f"Usando muestra aleatoria: {len(df)} filas (frac={args.sample_frac})")

    # Preprocesar
    print("Preprocesando textos (esto usa spaCy y puede tardar)...")
    df["clean_text"] = df[args.text_col].astype(str).map(lambda t: clean_text(t, nlp, stopwords_set))

    # Wordcloud general
    print("Generando wordcloud general...")
    wc_path = os.path.join(args.output, "wordclouds", "wordcloud_general.png")
    generate_wordcloud(df["clean_text"], wc_path, max_words=args.max_words)

    # Longitudes
    df["n_tokens"] = df["clean_text"].apply(lambda t: len(t.split()))
    lengths = df["n_tokens"].dropna().astype(int).values

    # Graficas
    print("Generando gráficos de longitudes...")
    plot_length_distributions(np.array(lengths), os.path.join(args.output, "plots", "lengths_hist.png"), os.path.join(args.output, "plots", "lengths_box.png"))

    # Top-k palabras
    print("Calculando top palabras...")
    all_words = " ".join(df["clean_text"].values).split()
    topk = Counter(all_words).most_common(args.topk)
    topk_df = pd.DataFrame(topk, columns=["word", "count"])
    topk_df.to_csv(os.path.join(args.output, "plots", "top_words.csv"), index=False)

    print("Proceso completo. Archivos guardados en:", args.output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generar wordclouds y análisis de longitudes (soporta en/es).")
    parser.add_argument("--input", required=True, help="Ruta al CSV de entrada")
    parser.add_argument("--text-col", default="text", help="Nombre de la columna con texto (ej: 'Text')")
    parser.add_argument("--output", default="outputs", help="Carpeta de salida")
    parser.add_argument("--max-words", type=int, default=200, help="Máximo de palabras en la wordcloud")
    parser.add_argument("--topk", type=int, default=50, help="Top K palabras a exportar")
    parser.add_argument("--sample-frac", type=float, default=1.0, help="Fracción de la muestra para pruebas (entre 0 y 1)")
    parser.add_argument("--lang", default="en", help="Idioma del texto: 'en' o 'es'")
    args = parser.parse_args()
    main(args)