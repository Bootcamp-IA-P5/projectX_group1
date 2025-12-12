# 🛡️ Project X - Detección de Lenguaje de Odio

<div align="center">

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green.svg)](https://fastapi.tiangolo.com/)
[![React 19](https://img.shields.io/badge/React-19-blue.svg)](https://react.dev/)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue?logo=docker)](https://docs.docker.com/compose/)

**Sistema de Clasificación de Textos para Detectar Lenguaje de Odio y Contenido Tóxico**

[Repositorio](https://github.com/Bootcamp-IA-P5/projectX_group1) • [Gestión](https://github.com/orgs/Bootcamp-IA-P5/projects/21/views/1) • [Contribuir](CONTRIBUTING.md)  •  [Presentación](https://gamma.app/docs/Proyecto-X-Radar-de-Toxicidad-zlvqwn7tlgxxqbj?mode=doc)

</div>

---

## 📋 Descripción

**Project X** es un detector inteligente de lenguaje de odio y contenido tóxico que funciona en **español e inglés**. 

Combina:
- 🔍 **Backend robusto** (FastAPI + clasificador keyword-based con contexto)
- 🎨 **Frontend moderno** (React + Vite con gráficos interactivos)
- 🐳 **Infraestructura containerizada** (Docker Compose)
- ⚡ **API REST** con healthchecks y manejo de errores

**Estado:** ✅ Producción (listo para entrega)
**Rama:** `feat/react-frontend` → `dev`
**Equipo:** Jimena, Ciprian, Ignacio, Kasthlen

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

### Opción 1: Docker Compose (Recomendado ⭐)

```bash
git clone https://github.com/Bootcamp-IA-P5/projectX_group1.git
cd projectX_group1

docker-compose up --build
```

Luego accede a:
- **Frontend:** http://localhost:8080
- **Backend API:** http://localhost:8000
- **Model Service:** http://localhost:8001

### Opción 2: Desarrollo Local

```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000

# Frontend (otra terminal)
cd frontend
npm install
npm run dev
```

Frontend en http://localhost:5173 con proxy automático al backend.

---

## 📁 Estructura del Proyecto

```
projectX_group1/
├── backend/
│   ├── app.py                 # FastAPI + clasificador mejorado
│   ├── infer.py               # Lógica de predicción
│   ├── toxic_keywords.py      # Palabras tóxicas con pesos (ES/EN)
│   ├── Dockerfile             # Imagen Docker
│   └── requirements.txt        # Dependencias
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx            # Componente principal
│   │   ├── App.css            # Estilos responsivos
│   │   └── main.jsx           # Entry point
│   ├── Dockerfile             # Build multi-stage + nginx
│   ├── nginx.conf             # Servidor web
│   ├── package.json           # Dependencias
│   └── vite.config.js         # Proxy config
│
├── model/
│   ├── app.py                 # Servicio de predicción
│   ├── Dockerfile
│   └── requirements-model.txt
│
├── docker-compose.yml         # Orquestación de servicios
├── README.md                  # Este archivo
├── DELIVERY.md                # Instrucciones de entrega
├── CHECKLIST.md               # Validación final
├── CONTRIBUTING.md            # Guía de contribución
├── MODEL_CARD.md              # Especificaciones del modelo
└── notebooks/                 # Análisis y EDA
```

---

## ✨ Características

### 🔍 Análisis Inteligente
- ✅ Detección de palabras tóxicas en español e inglés
- ✅ Análisis de contexto (negaciones, bromas, expresiones de cariño)
- ✅ Pesos de toxicidad personalizados (0.6 - 0.98)
- ✅ Puntuaciones de confianza (0.0 - 1.0)

### 🎨 Interfaz Moderna
- ✅ Diseño responsivo y atractivo
- ✅ Gráficos interactivos (Doughnut + Bar charts)
- ✅ Validación en tiempo real
- ✅ Manejo de errores elegante

### 🐳 Infraestructura
- ✅ Docker Compose con 3 servicios aislados
- ✅ Health checks automáticos
- ✅ CORS habilitado
- ✅ Nginx como reverse proxy

### 📊 API REST

```bash
POST /predict
Content-Type: application/json

{
  "text": "imbécil, no sabes cuanto te amo, daría mi vida por ti"
}
```

**Respuesta:**
```json
{
  "label": "safe",
  "score": 0.31
}
```

---

## 👥 Equipo

| Rol | Miembro |
|-----|---------|
| 🎯 Scrum Master | Ciprian |
| 📊 Product Owner | Ignacio |
| 💻 Developer | Jimena |
| 💻 Developer | Kasthlen |

---

## 🧪 Testing

```bash
# Health checks
curl http://localhost:8000/health
curl http://localhost:8001/health

# Predicción
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"imbécil careculo"}'
```

---

## 📚 Documentación

- **[DELIVERY.md](DELIVERY.md)** - Instrucciones de entrega final
- **[CHECKLIST.md](CHECKLIST.md)** - Validaciones completadas
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Guía de contribución
- **[MODEL_CARD.md](MODEL_CARD.md)** - Especificaciones del modelo

---

## 🔧 Desarrollo

### Pre-commit Hooks
```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

### Formato de Código
```bash
black .
isort .
```

### Commits
```bash
git commit -m "feat: descripción clara"
# Convenciones: feat, fix, chore, docs
```

---

## 🎯 Próximos Pasos

- [ ] Integración con modelo ML real (BERT, DistilBERT)
- [ ] Tests automatizados (pytest)
- [ ] CI/CD en GitHub Actions
- [ ] Deployment en servidor producción
- [ ] Monitoreo y métricas

---

<div align="center">

**Hecho con ❤️ por Grupo 1 | Bootcamp IA P5**

[GitHub](https://github.com/Bootcamp-IA-P5/projectX_group1) • [Project Board](https://github.com/orgs/Bootcamp-IA-P5/projects/21)
