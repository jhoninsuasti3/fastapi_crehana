# Usar una imagen base ligera de Python
FROM python:3.9-slim

# Configurar el directorio de trabajo
WORKDIR /app

# Copiar solo el archivo de dependencias para optimizar el cache de Docker
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código fuente al contenedor
COPY . .

# Exponer el puerto 8000 para FastAPI
EXPOSE 8000

# Comando de ejecución para FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
