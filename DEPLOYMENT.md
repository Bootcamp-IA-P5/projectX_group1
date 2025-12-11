# 🚀 Guía de Despliegue - Project X

## Inicio Rápido

### 1️⃣ Prerequisitos
- Docker 20.10+
- Docker Compose 1.29+
- Git

### 2️⃣ Desplegar en Producción

```bash
# Clonar repositorio
git clone https://github.com/Bootcamp-IA-P5/projectX_group1.git
cd projectX_group1

# Iniciar servicios
docker-compose up --build -d

# Verificar estado
docker ps
docker-compose logs -f
```

### 3️⃣ Verificar Servicios

```bash
# Health checks
curl http://localhost:8000/health      # Backend
curl http://localhost:8001/health      # Model Server
curl http://localhost:8080             # Frontend

# Test predicción
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "I hate you"}'
```

---

## 📊 Acceso a Interfaces

| Servicio | URL | Descripción |
|----------|-----|-------------|
| Frontend | http://localhost:8080 | Interfaz web para usuarios |
| Backend API | http://localhost:8000 | API REST (Swagger en /docs) |
| Model Server | http://localhost:8001 | Servicio de modelo auxiliar |
| Swagger Docs | http://localhost:8000/docs | Documentación interactiva |
| ReDoc | http://localhost:8000/redoc | Documentación alternativa |

---

## 🔧 Comandos Útiles

### Logs
```bash
# Todos los logs
docker-compose logs

# Logs en tiempo real
docker-compose logs -f

# Logs específicos
docker logs projectx-backend -f
docker logs projectx-frontend -f
docker logs projectx-model -f
```

### Administración
```bash
# Parar servicios
docker-compose down

# Parar y limpiar volumes
docker-compose down -v

# Reconstruir desde cero
docker-compose up --build -d

# Escalar servicios (si es necesario)
docker-compose up --scale backend=2 -d
```

### Testing
```bash
# Dentro del contenedor backend
docker exec projectx-backend python -c "import app; print('OK')"

# Ver modelos cargados
docker exec projectx-backend ls -lh /app/models/

# Test de predicción
docker exec projectx-backend python -c "
import requests
r = requests.post('http://localhost:8000/predict', json={'text': 'Kill yourself'})
print(r.json())
"
```

---

## 📈 Monitoreo

### Recursos
```bash
# CPU y memoria
docker stats

# Detalles de contenedor
docker inspect projectx-backend

# Historial de logs
docker logs --tail 100 projectx-backend
```

### Health Checks
Los health checks se ejecutan automáticamente cada 30s:
- Backend: Espera 40s antes del primer check
- Model: Espera 40s antes del primer check
- Frontend: No tiene health check

---

## 🚨 Troubleshooting

### Backend no inicia
```bash
# Ver errores específicos
docker logs projectx-backend

# Verificar puerto disponible
netstat -an | grep 8000

# Reconstruir limpio
docker-compose down -v
docker-compose up --build -d
```

### Frontend blanco/no carga
```bash
# Verificar CORS
docker logs projectx-backend | grep -i cors

# Verificar nginx
docker logs projectx-frontend

# Verificar conectividad
docker exec projectx-frontend curl http://backend:8000/health
```

### Modelo no carga
```bash
# Verificar archivos
docker exec projectx-backend ls -lh /app/models/

# Verificar permisos
docker exec projectx-backend stat /app/models/

# Ver error específico
docker logs projectx-backend | grep -i model
```

---

## 🔐 Seguridad

### Recomendaciones
- [ ] Cambiar contraseñas por defecto
- [ ] Usar HTTPS en producción
- [ ] Configurar firewall
- [ ] Limitar acceso a /docs y /redoc
- [ ] Usar reverse proxy (Nginx, Traefik)
- [ ] Implementar rate limiting
- [ ] Monitorear logs

### CORS
Frontend puede acceder a `http://localhost:8000` (configurable en `backend/app.py`)

---

## 📦 Escalado

### Docker Swarm
```bash
# Inicializar
docker swarm init

# Deploy stack
docker stack deploy -c docker-compose.yml projectx

# Escalar backend
docker service scale projectx_backend=3
```

### Kubernetes (opcional)
Se puede adaptar con Helm charts

---

## 🔄 Actualizaciones

### Actualizar código
```bash
git pull origin feat/react-frontend
docker-compose down
docker-compose up --build -d
```

### Actualizar modelo
```bash
# Entrenar nuevo modelo localmente
cd backend
python train_model.py
# Copiar archivos a models/

# Reconstruir
docker-compose up --build -d
```

---

## 📞 Soporte

- 📧 Contacto: grupo1@bootcamp-ia.dev
- 🐛 Reportar bugs: https://github.com/Bootcamp-IA-P5/projectX_group1/issues
- 💬 Discusiones: https://github.com/Bootcamp-IA-P5/projectX_group1/discussions

---

**Last Updated:** Diciembre 11, 2025
**Version:** 1.0.0
