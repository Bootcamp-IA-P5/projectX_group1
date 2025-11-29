# projectX_group1
proyecto de NLP para detectar lenguaje de odio

[gestión del proyecto](https://github.com/orgs/Bootcamp-IA-P5/projects/21/views/1)

## 📁 Estructura del Proyecto

```
projectX_group1/
│
├── data/                   # Datos del proyecto (no se suben a GitHub)
│   ├── raw/               # Datos originales sin procesar
│   └── processed/         # Datos limpios y transformados
│
├── models/                # Modelos entrenados (no se suben a GitHub)
│
├── notebooks/             # Jupyter notebooks para experimentación y análisis
│
├── backend/               # Código fuente del backend/API
│
└── README.md             # Este archivo
```

### 🗂️ Descripción de Carpetas

- **`data/raw/`**: Guarda aquí los datasets originales (CSV, JSON, etc.) tal como los descargas. Nunca modifiques estos archivos.

- **`data/processed/`**: Datasets después de limpieza, normalización, tokenización, etc. Listos para entrenar modelos.

- **`models/`**: Modelos entrenados (.pkl, .h5, .pt, etc.) y archivos relacionados (tokenizers, vectorizadores).

- **`notebooks/`**: Jupyter notebooks para exploración de datos (EDA), pruebas de modelos, visualizaciones.

- **`backend/`**: Código de producción, scripts, APIs, etc.

### ⚠️ Nota Importante

Las carpetas `data/` y `models/` están en `.gitignore`. Solo se sube la estructura (archivos `.gitkeep`), no el contenido. Esto evita subir archivos grandes a GitHub.
# Proyecto: Detección de Lenguaje de Odio (Project X - Group 1)

Resumen
-------
Breve descripción: este proyecto busca detectar lenguaje de odio y contenido tóxico en textos en español. La métrica principal utilizada es F1 (macro o ponderada según experimento).

Estado
------
- Estado: en desarrollo
- Rama principal para trabajo diario: `dev` (confirmar con el equipo)

Equipo
------
- Ciprian — Scrum Master
- Ignacio — Product Owner
- Jimena — Developer
- Kasthlen — Developer

Estructura del repositorio
--------------------------
- backend/            -> Código reutilizable (scripts de entrenamiento, utilidades, API)
- notebooks/          -> Notebooks de experimentos (limpios; outputs removidos)
- data/               -> Scripts/README para descarga de datos (no incluir datos sensibles)
- models/             -> Model cards y referencias (no incluir pesos grandes)
- outputs_spanish/    -> Resultados / salidas (no subir artefactos pesados)
- requirements.txt    -> Dependencias (usar versiones pinneadas)
- .pre-commit-config.yaml -> Hooks de pre-commit (formato, limpieza notebooks)
- README.md           -> Este archivo

Requisitos
----------
Instalación con virtualenv:
```bash
python -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

O con conda:
```bash
conda env create -f environment.yml
conda activate projectx
```

Datos
-----
No subir datasets con restricción. Proveer scripts en `data/`:
- data/README.md -> instrucciones y links
- scripts/download_data.sh -> script para descargar y verificar datos

Preprocesado
------------
Ejemplo:
```bash
python backend/preprocess.py --input data/raw --output data/processed
```

Entrenamiento y evaluación
--------------------------
Entrenar:
```bash
python backend/train.py --data-dir data/processed --output-dir models/exp1 --epochs 10 --batch-size 16
```

Evaluar:
```bash
python backend/evaluate.py --model models/exp1 --data data/processed/test.csv --out outputs/metrics.json
```

Docker y despliegue
-------------------
(Por confirmar)

Buenas prácticas y ética
-----------------------
- Revisar sesgos en los datos y posibles falsos positivos.
- No usar el modelo en decisiones críticas sin revisión humana.
- Mantener un MODEL_CARD con limitaciones y responsabilidad.

Contribuciones
-------------
Lee CONTRIBUTING.md para normas de contribución y hooks (pre-commit).

Licencia
--------
Añade aquí la licencia del proyecto (p. ej. MIT).

Contacto
--------
- Responsable del proyecto: correo@ejemplo.com
