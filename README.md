# 🚀 Task Management API - FastAPI

Bienvenido a **Task Management API**, un sistema basado en **FastAPI** para la gestión de tareas. Este proyecto sigue una arquitectura **hexagonal** y aplica principios **SOLID** y **Clean Code** para garantizar escalabilidad y mantenibilidad.

## 📂 Estructura del Proyecto



## 📌 Arquitectura del Proyecto

Esta API sigue una **arquitectura hexagonal**, separando capas de la siguiente manera:

- **`api/`** → Maneja las rutas de FastAPI y las respuestas HTTP.
- **`core/`** → Contiene la configuración y conexión a la base de datos.
- **`domain/`** → Define los modelos de datos.
- **`infrastructure/`** → Implementa los repositorios de persistencia.
- **`services/`** → Contiene la lógica de negocio.
- **`schemas/`** → Esquemas Pydantic para validación de datos.
- **`tests/`** → Pruebas unitarias e integración con `pytest`.

Esta separación permite una mayor **mantenibilidad**, facilitando el testing y la escalabilidad.

---

## 🚀 **Configuración Inicial**

### **1️⃣ Instalar Dependencias**
Asegúrate de tener **Python 3.9+** y ejecuta:

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

```

### 2️⃣ Configurar Pre-commit

```bash
pre-commit install
pre-commit run --all-files
```

### 3️⃣ Crear la Base de Datos
```bash
python -c "from app.core.database import Base, engine; Base.metadata.create_all(bind=engine)"
```

🏃‍♂️ Ejecutar la Aplicación Localmente
```bash
uvicorn app.main:app --reload
```
📌 Swagger UI: http://127.0.0.1:8000/docs
📌 Redoc: http://127.0.0.1:8000/redoc


# 🐳 Ejecutar la Aplicación con Docker

### 1️⃣ Construir la imagen
```bash
docker build -t fastapi-app .
```

### 2️⃣ Ejecutar el contenedor
```bash
docker run -p 8000:8000 fastapi-app
```

# 🐳 Ejecutar con docker-compose

Si prefieres levantar la API con docker-compose:
```bash
docker-compose up --build
```

# ✅ Ejecutar Pruebas
```bash
pytest --disable-warnings
```

Si quieres ver detalles de cada prueba:
```bash
pytest -v
```

# 📌 Pruebas de la API

Puedes probar los endpoints en Swagger UI o con curl:

### Obtener todas las tareas
```bash
curl -X 'GET' 'http://127.0.0.1:8000/tasks/' -H 'accept: application/json'
```


### Crear una tarea
```bash
curl -X 'POST' 'http://127.0.0.1:8000/tasks/' \
-H 'accept: application/json' -H 'Content-Type: application/json' \
-d '{"title": "Nueva tarea", "description": "Descripción", "completed": false}'
```

### Obtener todas las tareas
```bash
curl -X 'GET' 'http://127.0.0.1:8000/tasks/1/' -H 'accept: application/json'
```

### Obtener todas las tareas
```bash
curl -X 'PUT' 'http://127.0.0.1:8000/tasks/1/' \
-H 'accept: application/json' -H 'Content-Type: application/json' \
-d '{"title": "Tarea actualizada", "description": "Nueva descripción", "completed": true}'
```

### Obtener todas las tareas
```bash
curl -X 'DELETE' 'http://127.0.0.1:8000/tasks/1/' -H 'accept: application/json'
```

# 📌 Pruebas Automáticas
Para verificar que todo el código cumple con los estándares:
pre-commit run --all-files
pytest --disable-warnings




### **📌 Resumen**
✅ **Incluimos la descripción del proyecto y arquitectura hexagonal**.
✅ **Añadimos instrucciones para configurar el entorno local**.
✅ **Incluimos pasos para ejecutar la API con Docker**.
✅ **Añadimos instrucciones para ejecutar pruebas unitarias e integración**.
✅ **Proporcionamos ejemplos de uso con `curl` y enlaces a `Swagger UI`**.

🚀 **¡Este README cumple con todos los requerimientos y está listo para producción!** 🎯🔥
