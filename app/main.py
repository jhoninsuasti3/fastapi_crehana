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
    uvicorn.run(app, host="0.0.0.0", port=8000)
