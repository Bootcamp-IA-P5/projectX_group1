# 🚀 Project X - Hate Speech Detection

<div align="center">

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Pre-commit: enabled](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![Docker Compose](https://img.shields.io/badge/docker--compose-enabled-blue?logo=docker)](https://docs.docker.com/compose/)

**Detección de Lenguaje de Odio (Hate Speech & Toxic Content Detection)**

[Gestión del Proyecto](https://github.com/orgs/Bootcamp-IA-P5/projects/21/views/1) • [Issues](https://github.com/Bootcamp-IA-P5/projectX_group1/issues) • [Contribuir](CONTRIBUTING.md)

</div>

---

## 📋 Descripción

Este proyecto desarrolla un sistema de **clasificación de textos para detectar lenguaje de odio y contenido tóxico** en español e inglés. Utiliza técnicas de **NLP modernas** (transformers, fine-tuning) con métrica principal **F1-score**.

**Estado:** En desarrollo
**Rama principal:** `dev`
**Datos:** Datasets públicos como YouToxic y Spanish Hate Speech

---

## 👥 Equipo

| Rol | Miembro |
|-----|---------|
| 🎯 Scrum Master | Ciprian |
| 📊 Product Owner | Ignacio |
| 💻 Developer | Jimena |
| 💻 Developer | Kasthlen |

---

## 📁 Estructura del Proyecto

```
projectX_group1/
├── backend/                      # API y scripts de entrenamiento
│   ├── app.py                   # FastAPI application
│   ├── train.py                 # Script de entrenamiento
│   ├── infer.py                 # Inferencia y predicciones
│   ├── Dockerfile               # Containerización del backend
│   └── requirements.txt          # Dependencias del backend
│
├── frontend/                     # Interfaz de usuario
│   ├── static/
│   │   └── index.html           # Frontend HTML/CSS/JS
│   └── Dockerfile               # Containerización del frontend
│
├── model/                        # Servicio de modelo
│   ├── app.py                   # API del modelo
│   ├── Dockerfile               # Containerización del modelo
│   └── requirements-model.txt    # Dependencias del modelo
│
├── notebooks/                    # Análisis y experimentación
│   ├── 01_exploratory_data_analysis.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_wordcloud_and_lengths.ipynb
│   └── scripts/
│       └── wordcloud_lengths.py
│
├── data/                         # Datasets (gitignored)
│   ├── raw/                     # Datos originales
│   └── processed/               # Datos limpios
│
├── outputs_spanish/              # Resultados de experimentos
│   └── plots/, wordclouds/
│
├── docker-compose.yml            # Orquestación de servicios
├── requirements.txt              # Dependencias principales
├── requirements-prod.txt         # Dependencias de producción
├── .pre-commit-config.yaml      # Hooks de pre-commit
├── MODEL_CARD.md                # Especificaciones del modelo
├── CONTRIBUTING.md              # Guía de contribución
└── README.md                    # Este archivo
```

---

## 🚀 Inicio Rápido

### Requisitos Previos
- **Python 3.10+**
- **Docker & Docker Compose** (opcional, recomendado)
- **Git**

### Opción 1: Instalación Local

```bash
# Clonar repositorio
git clone https://github.com/Bootcamp-IA-P5/projectX_group1.git
cd projectX_group1

# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Pre-commit hooks (recomendado)
pip install pre-commit
pre-commit install
```

### Opción 2: Docker Compose (Recomendado)

```bash
# Clonar repositorio
git clone https://github.com/Bootcamp-IA-P5/projectX_group1.git
cd projectX_group1

# Iniciar servicios
docker-compose up --build

# Acceder a:
# Frontend: http://localhost:8080
# Backend API: http://localhost:8000
# Model Service: http://localhost:8001
```

---

## 📊 Flujo de Trabajo

### 1. **Exploración de Datos (EDA)**
```bash
jupyter notebook notebooks/01_exploratory_data_analysis.ipynb
```

### 2. **Preprocesamiento**
```bash
python backend/train.py --mode preprocess --data-dir data/raw --output-dir data/processed
```

### 3. **Entrenamiento**
```bash
python backend/train.py \
  --data-dir data/processed \
  --output-dir models/exp1 \
  --epochs 10 \
  --batch-size 16
```

### 4. **Inferencia**
```bash
python backend/infer.py --model-path models/exp1 --text "Ejemplo de texto"
```

### 5. **API Local**
```bash
# Backend
cd backend && uvicorn app:app --host 0.0.0.0 --port 8000

# Model Service
cd model && python app.py
```

---

## 🐳 Docker Compose

Estructura de servicios aislados para mejor mantenibilidad:

| Servicio | Puerto | Descripción |
|----------|--------|-------------|
| **frontend** | 8080 | Interfaz de usuario |
| **backend** | 8000 | API FastAPI |
| **model** | 8001 | Servicio de modelo |

**Health Checks:** Todos los servicios incluyen verificaciones de salud automáticas.

```bash
# Ver logs
docker-compose logs -f backend

# Detener servicios
docker-compose down
```

---

## 💻 Desarrollo

### Formato de Código
```bash
# Black (formateador)
black .

# isort (organizador de imports)
isort .

# Pre-commit (automático)
pre-commit run --all-files
```

### Tests
```bash
pip install pytest
pytest tests/ -v
```

### Notebooks
- ⚠️ Mantén los notebooks sin outputs (pre-commit los limpiará automáticamente)
- 📌 Usa `nbstripout` para limpiar manualmente si es necesario

---

## 📝 Contribuir

Ver [CONTRIBUTING.md](CONTRIBUTING.md) para:
- 🔄 Flujo de branching (feat/, fix/, chore/)
- 📋 Convenciones de commits
- 🔍 Proceso de Pull Requests
- ✅ Checklist de calidad

**Pasos rápidos:**
```bash
git checkout -b feat/mi-feature dev
# hacer cambios...
git add .
git commit -m "feat: descripción clara"
git push origin feat/mi-feature
# Abrir PR hacia dev
```

---

## 📦 Dependencias

**Principales:**
- `transformers` - Modelos NLP pre-entrenados
- `fastapi` - Framework para API
- `torch` / `tensorflow` - Deep Learning
- `pandas`, `numpy` - Procesamiento de datos
- `scikit-learn` - Métricas y utilidades ML

Ver `requirements.txt` y `requirements-prod.txt` para versiones exactas.

---

## 📊 Model Card

Ver [MODEL_CARD.md](MODEL_CARD.md) para:
- 📈 Métricas de desempeño
- ⚠️ Limitaciones y sesgos
- 🔧 Cómo usar el modelo
- 📋 Consideraciones éticas

---

## ⚖️ Licencia

[Especificar licencia del proyecto]

---

## 📞 Contacto & Soporte

- **GitHub Issues:** [Reportar bugs](https://github.com/Bootcamp-IA-P5/projectX_group1/issues)
- **Discussions:** [Preguntas y sugerencias](https://github.com/Bootcamp-IA-P5/projectX_group1/discussions)

---

## 🎯 Hoja de Ruta

- [ ] Finalizar EDA y preprocesamiento
- [ ] Entrenar modelo base
- [ ] Implementar API backend
- [ ] Desarrollar interfaz frontend
- [ ] Evaluación y optimización
- [ ] Documentación final
- [ ] Deployment en producción

---

<div align="center">

**Made with ❤️ by Group 1 | Bootcamp IA P5**

</div>

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
