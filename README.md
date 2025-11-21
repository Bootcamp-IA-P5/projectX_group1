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
