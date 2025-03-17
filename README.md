# 🚀 Task Management API - FastAPI

Bienvenido a **Task Management API**, un sistema basado en **FastAPI** para la gestión de tareas. Este proyecto sigue una arquitectura **hexagonal** y aplica principios **SOLID** y **Clean Code** para garantizar escalabilidad y mantenibilidad.

## 📂 Estructura del Proyecto

# 🚀 Task Management API - FastAPI

Bienvenido a **Task Management API**, un sistema basado en **FastAPI** para la gestión de tareas. Este proyecto sigue una arquitectura **hexagonal** y aplica principios **SOLID** y **Clean Code** para garantizar escalabilidad y mantenibilidad.

## 📂 Estructura del Proyecto




## 🚀 Configuración Inicial

### 1️⃣ **Instalar Dependencias**

Asegúrate de tener **Python 3.9+** y ejecuta:


---

### **📌 ¿Cómo Configurar Todo Inicialmente?**
Ejecuta estos comandos **una sola vez** después de clonar el proyecto:

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar pre-commit
pre-commit install
pre-commit run --all-files

# Ejecutar el servidor
uvicorn app.main:app --reload
```