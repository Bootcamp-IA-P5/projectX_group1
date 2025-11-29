FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc git ca-certificates \
  && rm -rf /var/lib/apt/lists/*

# Copiar e instalar solo dependencias de producción
COPY requirements-prod.txt /app/requirements-prod.txt
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements-prod.txt

# Copiar el código
COPY . /app

RUN useradd -m appuser && chown -R appuser /app
USER appuser

EXPOSE 8000
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]
