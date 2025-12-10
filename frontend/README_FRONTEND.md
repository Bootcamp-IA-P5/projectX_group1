# Frontend - React + Vite

Interfaz moderna y responsiva para análisis de lenguaje de odio.

## 🚀 Quick Start

### Desarrollo
```bash
npm install
npm run dev
```

Abre [http://localhost:5173](http://localhost:5173)

### Build
```bash
npm run build
npm run preview
```

### Docker
```bash
docker build -t projectx-frontend .
docker run -p 8080:80 projectx-frontend
```

## 📦 Tech Stack

- **React 19** - UI Library
- **Vite** - Build tool & dev server
- **Chart.js** - Gráficos interactivos
- **Nginx** - Production server
- **ESLint** - Linting

## 🎨 Features

- ✅ Análisis en tiempo real
- ✅ Gráficos interactivos (Doughnut + Bar)
- ✅ Diseño 100% responsivo
- ✅ Validación de entrada
- ✅ Manejo elegante de errores
- ✅ Proxy automático al backend

## 📡 API Integration

Comunica con `/api/predict`:

```javascript
const response = await fetch('/api/predict', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ text: userInput })
})
```

## 🔧 Configuration

Crear `.env` (opcional):
```env
VITE_API_URL=http://localhost:8000
```

## 📁 Structure

```
frontend/
├── src/
│   ├── App.jsx          # Componente principal
│   ├── App.css          # Estilos
│   ├── index.css        # Global styles
│   └── main.jsx         # Entry point
├── public/              # Static assets
├── Dockerfile           # Multi-stage build
├── nginx.conf           # Server config
└── package.json         # Dependencies
```

---

Made with ❤️ for Project X | Bootcamp IA P5
