# 📦 Project X - Entrega Final

**Bootcamp IA P5 | Group 1**

## 👥 Equipo

| Rol | Participante |
|-----|-------------|
| 🎯 Scrum Master | Ciprian |
| 📊 Product Owner | Ignacio |
| 💻 Developer | Jimena |
| 💻 Developer | Kasthlen |

---

## 🚀 Quick Start

### Backend
```bash
cd c:\Users\Coder\OneDrive\ -\ uniminuto.edu\curso-programacion\bootcamp_ia\NLP\projectX_group1
python backend/server.py
```
- Servidor en: `http://localhost:8000`
- Health check: `http://localhost:8000/health`
- Endpoint: `POST http://localhost:8000/predict`

### Frontend
```bash
cd frontend
npm install
npm run dev
```
- Aplicación en: `http://localhost:5173`
- Auto-refresca con cambios (HMR)
- Proxy automático al backend

---

## 📋 Características Implementadas

### ✅ Backend
- **Servidor HTTP** robusto con manejo de CORS
- **Clasificador de palabras tóxicas** mejorado:
  - Patrones regex en español e inglés
  - Pesos de toxicidad (0.6-0.98)
  - Detección de contexto seguro (negaciones, bromas)
  - Soporte para múltiples palabras tóxicas
- **Fallback keyword classifier** cuando el modelo real no esté disponible
- **Respuestas JSON** estructuradas con métricas

### ✅ Frontend
- **UI moderna** con gradientes y diseño responsivo
- **Análisis en tiempo real** con validación
- **Gráficos interactivos**:
  - Doughnut chart: Nivel de confianza
  - Bar chart: Distribución de probabilidades
  - Barras lineales: Detalles de probabilidad
- **UX mejorada**:
  - Contador de caracteres
  - Estados de carga
  - Manejo de errores
  - Formulario limpio

### ✅ Infraestructura
- **Docker Compose** con servicios aislados
- **Dockerfiles** para frontend (nginx) y backend
- **Pre-commit hooks** configurados (black, isort, nbstripout)
- **Nginx config** con proxy a backend
- **Scripts de inicio** para desarrollo (.bat/.sh)

---

## 🏗️ Estructura del Proyecto

```
projectX_group1/
├── backend/
│   ├── server.py              # Servidor HTTP principal
│   ├── toxic_keywords.py      # Configuración de palabras tóxicas
│   ├── infer.py               # Lógica de inferencia
│   ├── Dockerfile             # Containerización
│   └── requirements.txt        # Dependencias
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx            # Componente principal
│   │   ├── App.css            # Estilos (responsive)
│   │   └── main.jsx           # Entry point
│   ├── Dockerfile             # Build multi-stage + nginx
│   ├── nginx.conf             # Configuración servidor
│   ├── package.json           # Dependencias (React, Vite, Chart.js)
│   └── vite.config.js         # Proxy config
│
├── docker-compose.yml         # Orquestación de servicios
├── README.md                  # Documentación completa
├── MODEL_CARD.md              # Especificaciones del modelo
├── CONTRIBUTING.md            # Guía de contribución (actualizada)
│
├── notebooks/                 # Análisis y EDA
├── data/                      # Datasets (gitignored)
└── outputs_spanish/           # Resultados previos
```

---

## 🧪 Testing

### Backend
```bash
# Test endpoint salud
curl http://localhost:8000/health

# Test predicción
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"imbécil careculo"}'
```

### Frontend
```bash
npm run lint      # Verificar código
npm run build     # Build para producción
npm run preview   # Ver build producción
```

---

## 📊 Modelo Actual

**Tipo:** Keyword-based classifier (fallback)

**Patrones Detectados:**
- 🇪🇸 Español: imbécil, careculo, cabrón, puto/puta, etc.
- 🇬🇧 Inglés: fuck, shit, bitch, asshole, etc.

**Métricas:**
- Toxicity threshold: 0.6
- Pesos de palabras: 0.6-0.98
- Contexto seguro: reduce toxicidad 50%
- Múltiples matches: +0.1 al score

---

## 🔄 Workflow de Desarrollo

### Crear feature
```bash
git checkout -b feat/nombre-feature dev
```

### Commitear con convenciones
```bash
git commit -m "feat: descripción corta
- Detalle 1
- Detalle 2"
```

### Pre-commit hooks automáticos
- black (formateo Python)
- isort (orden imports)
- nbstripout (limpiar notebooks)
- trim trailing whitespace
- check YAML

### PR a dev
1. Pushear rama
2. Crear PR en GitHub
3. Esperar revisión
4. Merge después de ✅

---

## 🐳 Docker

### Build local
```bash
docker-compose build
docker-compose up
```

### Servicios
- **frontend**: Puerto 8080 (nginx)
- **backend**: Puerto 8000
- **model**: Puerto 8001 (cuando esté listo)

---

## 📝 Notas Importantes

- ✅ Frontend y backend están completamente funcionales
- ✅ El clasificador detecta lenguaje tóxico correctamente
- ✅ Gráficos muestran probabilidades en tiempo real
- ✅ Todo documentado en README.md
- ⚠️ El modelo actual es keyword-based (fallback)
- 🎯 Para producción, reemplazar con modelo ML entrenado

---

## 📚 Documentación Adicional

- [README.md](README.md) - Guía completa del proyecto
- [MODEL_CARD.md](MODEL_CARD.md) - Especificaciones del modelo
- [CONTRIBUTING.md](CONTRIBUTING.md) - Guía para contribuidores
- [frontend/README_FRONTEND.md](frontend/README_FRONTEND.md) - Docs específicas del frontend

---

## ✨ Estado del Proyecto

**Rama actual:** `feat/react-frontend`
**Commits:** ✅ Listos para merge
**Tests:** ✅ Funciona correctamente
**Documentación:** ✅ Completa

**Próximos pasos:**
1. Merge de `feat/react-frontend` → `dev`
2. Entrega final del proyecto
3. (Opcional) Deployment en producción

---

**Última actualización:** 10 de Diciembre de 2025
**Estado:** 🟢 Listo para entrega
