import os
from fastapi import FastAPI
from app.api.routes.task_routes import router as task_router
from app.api.error_handlers import setup_error_handlers

app = FastAPI(title="Task Management API")

# Incluir Rutas
app.include_router(task_router, prefix="/tasks", tags=["Tasks"])

# Configurar manejo de errores
setup_error_handlers(app)


if __name__ == "__main__":
    import uvicorn

    host = "0.0.0.0" if os.getenv("ENV") == "dev" else "127.0.0.1"
    uvicorn.run(app, host=host, port=8000)  # Configuración segura
