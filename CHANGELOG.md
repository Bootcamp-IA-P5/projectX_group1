# 📝 CHANGELOG - Project X

Todos los cambios importantes en este proyecto serán documentados en este archivo.

---

## [1.0.0] - 2025-12-11

### ✨ Características Principales

#### Backend
- ✅ FastAPI REST API con endpoints `/health` y `/predict`
- ✅ Machine Learning model (LogisticRegression + TF-IDF)
- ✅ Model serving con joblib
- ✅ CORS habilitado para frontend
- ✅ Validación Pydantic
- ✅ Health checks automáticos
- ✅ Preprocesamiento de texto (emoji, stopwords, lemmatización)

#### Frontend
- ✅ React 19 SPA responsiva
- ✅ Interfaz intuitiva para predicciones
- ✅ Gráficos interactivos (Chart.js)
- ✅ Historial de predicciones
- ✅ Validación en cliente
- ✅ Manejo de errores elegante

#### DevOps
- ✅ Docker Compose con 3 servicios
- ✅ Health checks con retries
- ✅ Networking aislado
- ✅ Non-root users
- ✅ Multi-stage builds

### 📊 Modelo ML

- **Dataset:** YouToxic 1000 (462 toxic, 538 safe)
- **Train Accuracy:** 79.75%
- **Test Accuracy:** 71.5%
- **Features:** TF-IDF (250 dimensiones)
- **Algoritmo:** LogisticRegression con class_weight='balanced'

### 🐛 Correcciones Iniciales

- [x] Fix: Corrección de ruta en Dockerfile (uvicorn backend.app:app)
- [x] Fix: Modelos no incluidos en Docker (.dockerignore)
- [x] Fix: ImportError de módulos en Docker (consolidación en app.py)

### 📚 Documentación

- ✅ README.md con inicio rápido
- ✅ DEPLOYMENT.md con guía de despliegue
- ✅ MODEL_CARD.md con especificaciones ML
- ✅ CONTRIBUTING.md con guía de contribución
- ✅ CHANGELOG.md (este archivo)

### 🔧 Configuración

- Python 3.10-slim
- FastAPI 0.110+
- React 19 con Vite
- scikit-learn para ML
- NLTK para preprocesamiento
- Docker & Docker Compose

---

## [Versiones Futuras] - Planificado

### [1.1.0] - Planned
- [ ] Integración con BERT/DistilBERT
- [ ] Tests unitarios (pytest)
- [ ] CI/CD en GitHub Actions
- [ ] Soporte multiidioma

### [1.2.0] - Planned
- [ ] Deployment en AWS/GCP
- [ ] Dashboard de monitoreo
- [ ] Rate limiting
- [ ] Caché de predicciones

### [2.0.0] - Planned
- [ ] Arquitectura de microservicios
- [ ] Kubernetes support
- [ ] GraphQL API
- [ ] WebSocket para predicciones en tiempo real

---

## Convenciones de Versionado

Este proyecto sigue [Semantic Versioning](https://semver.org/):

- **MAJOR:** Cambios incompatibles con API
- **MINOR:** Nuevas funcionalidades compatibles
- **PATCH:** Correcciones de bugs

### Format: `MAJOR.MINOR.PATCH`
- 1.0.0 = Primera versión estable
- 1.0.1 = Bug fix
- 1.1.0 = Nueva característica
- 2.0.0 = Cambios mayores

---

## Notas de Desarrollo

### Estructura de Commits
```
feat: Nueva característica
fix: Corrección de bug
chore: Cambios en build, CI/CD
docs: Cambios en documentación
test: Agregar/modificar tests
refactor: Refactorización sin cambios funcionales
perf: Mejoras de rendimiento
```

### Branch Strategy
- `main` → Versiones estables
- `dev` → Desarrollo activo
- `feat/feature-name` → Desarrollo de características
- `fix/bug-name` → Correcciones de bugs

---

**Última actualización:** Diciembre 11, 2025
