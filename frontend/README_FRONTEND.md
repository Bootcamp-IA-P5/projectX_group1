# Frontend - React + Vite

Frontend application for hate speech detection built with React, Vite, and modern web technologies.

## 🚀 Quick Start

### Development
```bash
npm install
npm run dev
```

Open [http://localhost:5173](http://localhost:5173)

### Build for Production
```bash
npm run build
npm run preview
```

### Docker
```bash
docker build -t projectx-frontend .
docker run -p 80:80 projectx-frontend
```

## 📦 Tech Stack

- **React 19** - UI Library
- **Vite** - Build tool & dev server
- **Nginx** - Production server
- **ESLint** - Code linting

## 🔧 Configuration

Create a `.env` file (copy from `.env.example`):

```bash
VITE_API_URL=http://localhost:8000
```

## 📁 Structure

```
frontend/
├── src/
│   ├── App.jsx          # Main application component
│   ├── App.css          # Application styles
│   ├── index.css        # Global styles
│   └── main.jsx         # Entry point
├── public/              # Static assets
├── Dockerfile           # Docker configuration
├── nginx.conf           # Nginx server config
└── package.json         # Dependencies
```

## 🎨 Features

- ✅ Real-time text analysis
- ✅ Confidence score visualization
- ✅ Probability bars for predictions
- ✅ Responsive design
- ✅ Error handling
- ✅ Loading states

## 🐳 Docker Deployment

Multi-stage build for optimized production:
- Build stage: Compiles React app
- Production stage: Serves with Nginx

## 📝 API Integration

The frontend communicates with the backend API:
- `POST /api/predict` - Analyze text for hate speech

## 🤝 Contributing

See main [CONTRIBUTING.md](../CONTRIBUTING.md)
