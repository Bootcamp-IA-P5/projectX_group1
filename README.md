# 🛡️ Project X - Detección de Lenguaje Tóxico (Hate Speech Detection)

<div align="center">

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green.svg)](https://fastapi.tiangolo.com/)
[![React 19](https://img.shields.io/badge/React-19-blue.svg)](https://react.dev/)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue?logo=docker)](https://docs.docker.com/compose/)
[![Scikit-learn](https://img.shields.io/badge/Scikit_learn-ML-orange.svg)](https://scikit-learn.org/)

**Sistema de Clasificación de Textos para Detectar Lenguaje Tóxico usando Machine Learning**

[Repositorio](https://github.com/Bootcamp-IA-P5/projectX_group1) • [Gestión](https://github.com/orgs/Bootcamp-IA-P5/projects/21/views/1) • [Contribuir](CONTRIBUTING.md)

</div>

---

## 📋 Descripción

**Project X** es un detector de lenguaje tóxico basado en **Machine Learning** que utiliza:

- 🤖 **Modelo ML:** LogisticRegression + TF-IDF Vectorizer (scikit-learn)
- 📊 **Dataset:** YouToxic English 1000 (462 tóxico, 538 seguro)
- 📈 **Rendimiento:** 79.75% accuracy train | 71.5% accuracy test
- 🔍 **Preprocesamiento:** NLTK stemming + emoji demojización + stopwords removal
- 🌍 **Idioma:** English (extensible a español)

**Stack Técnico:**
- 🔍 **Backend:** FastAPI + Python 3.10 + joblib model serving
- 🎨 **Frontend:** React 19 + Vite + Responsive Design + Chart.js
- 🐳 **DevOps:** Docker Compose (3 servicios)
- ⚡ **API:** REST endpoints con validación Pydantic

**Estado:** ✅ **Completamente funcional en producción**

---

## 👥 Equipo

| Rol | Miembro |
|-----|---------|
| 🎯 Scrum Master | Ciprian |
| 📊 Product Owner | Ignacio |
| 💻 Developer | Jimena |
| 💻 Developer | Kasthlen |

---

## 🚀 Inicio Rápido

### Opción 1: Docker Compose (✅ Recomendado - Producción)

```bash
# Clonar repositorio
git clone https://github.com/Bootcamp-IA-P5/projectX_group1.git
cd projectX_group1

# Iniciar todos los servicios
docker-compose up --build -d

# Verificar salud de servicios
docker ps
```

**Servicios disponibles:**
| Servicio | URL | Status |
|----------|-----|--------|
| 🎨 Frontend | http://localhost:8080 | ✅ Healthy |
| 🔌 Backend API | http://localhost:8000 | ✅ Healthy |
| 🤖 Model Server | http://localhost:8001 | ✅ Healthy |

### Opción 2: Desarrollo Local

```bash
# Backend
cd backend
pip install -r requirements.txt
python train_model.py          # Entrenar modelo (opcional)
uvicorn app:app --reload --host 0.0.0.0 --port 8000

# Frontend (otra terminal)
cd frontend
npm install
npm run dev
```

Frontend en http://localhost:5173

---

## 🎯 Uso

### API Endpoints

**Health Check:**
```bash
curl http://localhost:8000/health
# Response: {"status": "ok"}
```

**Predicción de Texto:**
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "I hate this stupid thing"}'

# Response:
# {
#   "label": "toxic",
#   "score": 0.547
# }
```

**Ejemplos de Predicciones:**
```
"This is a wonderful day"      → safe   (0.485)
"You are stupid"               → toxic  (0.561)
"I love this movie"            → safe   (0.459)
"Kill yourself"                → toxic  (0.514)
```

### Frontend (http://localhost:8080)
- 📝 Ingresa texto a analizar
- 🎯 Clasificación instantánea (tóxico/seguro)
- 📊 Gráficos interactivos en tiempo real
- 🔄 Historial de predicciones

---

## 📁 Estructura del Proyecto

```
projectX_group1/
├── backend/                           # FastAPI + ML Backend
│   ├── app.py                        # FastAPI con endpoints /health, /predict
│   ├── train_model.py                # Script entrenamiento LogisticRegression
│   ├── Dockerfile                    # CMD: uvicorn backend.app:app
│   └── requirements.txt              # fastapi, scikit-learn, joblib, nltk, emoji
│
├── frontend/                         # React + Vite SPA
│   ├── static/
│   │   └── index.html               # Interfaz web responsiva
│   ├── Dockerfile                   # Build multi-stage nginx
│   ├── nginx.conf                   # Config servidor web
│   └── package.json                 # React, axios, chart.js
│
├── model/                            # Servicio auxiliar
│   ├── app.py                       # Health check endpoint
│   ├── Dockerfile
│   └── requirements-model.txt
│
├── models/                           # Modelos ML persistentes
│   ├── logreg_C0.0001_feat250_aug5.joblib
│   └── logreg_C0.0001_feat250_aug5_vectorizer.joblib
│
├── data/processed/                  # Datasets
│   ├── youtoxic_english_1000.csv    # 462 toxic + 538 safe
│   └── spanish_sample.csv
│
├── notebooks/                       # Análisis y EDA
│   ├── 01_exploratory_data_analysis.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_wordcloud_and_lengths.ipynb
│   └── scripts/wordcloud_lengths.py
│
├── src/                             # Módulos de preprocesamiento
│   ├── preprocessing.py             # Shared preprocessing functions
│   └── augmentation.py              # Data augmentation
│
├── docker-compose.yml               # Orquestación (3 servicios)
├── .dockerignore                    # Exclusions
├── README.md                        # Este archivo
├── CONTRIBUTING.md                  # Guía de contribución
├── MODEL_CARD.md                    # Especificaciones ML
└── requirements.txt                 # Dependencias root
```

---

## 🤖 Modelo ML

### Arquitectura
```
Input Text
    ↓
[Preprocesamiento: Demoji + Lowercase + Tokenization + Lemmatization]
    ↓
TF-IDF Vectorizer (max_features=250, ngrams=(1,2))
    ↓
LogisticRegression (C=0.1, class_weight='balanced')
    ↓
Output: {label: 'toxic'|'safe', score: float[0-1]}
```

### Rendimiento
- **Dataset:** YouToxic 1000 muestras
  - Train: 800 (375 toxic, 425 safe)
  - Test: 200 (87 toxic, 113 safe)
- **Train Accuracy:** 79.75%
- **Test Accuracy:** 71.5%
- **Threshold:** 0.5 (score >= 0.5 → toxic)

### Preprocesamiento
1. Demojización (emoji → texto descriptivo)
2. Conversión a minúsculas
3. Tokenización por espacios
4. Eliminación de caracteres especiales
5. Stopwords removal (NLTK English)
6. Lemmatización (NLTK WordNetLemmatizer)

---

## 🏗️ Características Técnicas

### Backend (FastAPI)
- ✅ Endpoints: `/health` (GET), `/predict` (POST)
- ✅ Validación Pydantic (TextRequest schema)
- ✅ Lazy loading de modelos joblib
- ✅ CORS habilitado para frontend
- ✅ Health checks con retries automáticos
- ✅ Manejo robusto de errores
- ✅ Logs estructurados

### Frontend (React)
- ✅ Componentes funcionales con hooks
- ✅ Diseño responsivo (mobile-first)
- ✅ Gráficos interactivos (Chart.js Doughnut + Bar)
- ✅ Validación de input cliente
- ✅ Error handling elegante
- ✅ UX intuitiva con feedback instantáneo

### Infraestructura (Docker)
- ✅ 3 servicios independientes en red aislada
- ✅ Health checks con retries
- ✅ Volumes persistentes para modelos
- ✅ Non-root users (seguridad)
- ✅ Multi-stage builds (frontend)
- ✅ .dockerignore optimizado

---

## 🧪 Testing

```bash
# Health checks
curl http://localhost:8000/health
curl http://localhost:8001/health

# Predicción
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"Kill yourself"}'

# Ver logs
docker logs projectx-backend
docker logs projectx-frontend
docker logs projectx-model
```

---

## 📚 Documentación

- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Guía de contribución
- **[MODEL_CARD.md](MODEL_CARD.md)** - Especificaciones del modelo
- **[DELIVERY.md](DELIVERY.md)** - Instrucciones de entrega
- **[CHECKLIST.md](CHECKLIST.md)** - Validaciones completadas

---

## 🔧 Desarrollo

### Pre-commit Hooks
```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

### Entrenar nuevo modelo
```bash
cd backend
python train_model.py
# Genera: models/logreg_*.joblib y *_vectorizer.joblib
```

### Commits
```bash
git commit -m "feat: descripción clara"
# Convenciones: feat, fix, chore, docs, test
```

---

## 🚨 Troubleshooting

### Backend no inicia
```bash
# Verificar logs
docker logs projectx-backend

# Reconstruir limpio
docker-compose down -v
docker-compose up --build -d
```

### Frontend no conecta con backend
- Verificar CORS en `backend/app.py`
- Verificar URL en `frontend/static/index.html`
- Revisar logs: `docker logs projectx-backend`

### Modelo no carga
- Verificar `.dockerignore` permite `/models/`
- Verificar path en `app.py`: `/app/models/`
- Reconstruir: `docker-compose up --build -d`

---

## 📊 Métricas

| Métrica | Valor |
|---------|-------|
| Accuracy (train) | 79.75% |
| Accuracy (test) | 71.5% |
| Dataset size | 1000 |
| Feature dimensions (TF-IDF) | 250 |
| Model size | ~200KB |
| Inference time | <100ms |

---

## 🎯 Roadmap

- [ ] Integración con modelos BERT/DistilBERT
- [ ] Tests unitarios (pytest)
- [ ] CI/CD en GitHub Actions
- [ ] Deployment en AWS/GCP
- [ ] Soporte multiidioma
- [ ] Dashboard de monitoreo
- [ ] Rate limiting

---

<div align="center">

**Hecho con ❤️ por Grupo 1 | Bootcamp IA P5**

[GitHub](https://github.com/Bootcamp-IA-P5/projectX_group1) • [Project Board](https://github.com/orgs/Bootcamp-IA-P5/projects/21)

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Made with React](https://img.shields.io/badge/Made%20with-React-61DAFB?logo=react&logoColor=white)](https://react.dev/)

</div>
