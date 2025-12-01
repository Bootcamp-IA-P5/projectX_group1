# Contributing

Gracias por contribuir. Por favor sigue estas pautas para facilitar revisiones y calidad del proyecto.

1. Flujo de trabajo
- Crea una rama a partir de `dev` (o `main`) con un nombre descriptivo:
  - feat/mi-feature
  - fix/issue-descripcion

2. Entorno
- Usa el environment.yml o requirements.txt:
  ```bash
  conda env create -f environment.yml
  conda activate projectx
  # o:
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  ```

3. Hooks y formato
- Pre-commit ya está configurado. Instálalo localmente:
  ```bash
  pip install pre-commit
  pre-commit install
  pre-commit run --all-files
  ```
- Usa `black` y `isort` para formateo de código.

4. Notebooks
- Mantén los notebooks limpios de outputs. El pre-commit y nbstripout harán limpieza automática, pero revisa antes de commitear.
- Si necesitas guardar resultados pesados, almacénalos fuera del repo (Drive / S3) y añade scripts de descarga.

5. Tests
- Añade tests en `tests/` y ejecútalos con `pytest`.
  ```bash
  pip install pytest
  pytest -q
  ```

6. Pull Requests
- Abre PR hacia `dev` (o la rama acordada).
- Incluye descripción, pasos para reproducir, archivos cambiados y checklist.

7. Estilo de commits
- Usa mensajes claros:
  - feat: descripción corta
  - fix: descripción corta
  - chore: tareas de mantenimiento
