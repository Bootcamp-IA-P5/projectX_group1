"""
Script placeholder para entrenar un modelo.
Sustituye por la lógica de entrenamiento real (cargar datos, modelo, guardar pesos).
"""

import argparse


def main(args):
    print(
        "Entrenamiento placeholder. Implementa la función de entrenamiento real aquí."
    )
    print(f"Data dir: {args.data_dir} - Output dir: {args.output_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", default="data/processed")
    parser.add_argument("--output-dir", default="models/exp1")
    args = parser.parse_args()
    main(args)
