from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.services.task_service import TaskService
from app.schemas.task_schema import TaskSchema, TaskResponse

router = APIRouter()

# Dependencia para la sesión de la BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📌 Obtener todas las tareas
@router.get("/", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return TaskService.get_all_tasks(db)

# 📌 Crear una nueva tarea
@router.post("/", response_model=TaskResponse)
def create_task(task: TaskSchema, db: Session = Depends(get_db)):
    return TaskService.create_task(db, task)

# 📌 Obtener una tarea por ID
@router.get("/{id}/", response_model=TaskResponse)
def get_task(id: int, db: Session = Depends(get_db)):
    task = TaskService.get_task_by_id(db, id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# 📌 Actualizar una tarea por ID
@router.put("/{id}/", response_model=TaskResponse)
def update_task(id: int, updated_task: TaskSchema, db: Session = Depends(get_db)):
    task = TaskService.update_task(db, id, updated_task)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# 📌 Eliminar una tarea por ID
@router.delete("/{id}/")
def delete_task(id: int, db: Session = Depends(get_db)):
    if not TaskService.delete_task(db, id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}
