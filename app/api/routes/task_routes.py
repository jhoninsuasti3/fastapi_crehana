from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.services.task_service import TaskService
from app.schemas.task_schema import TaskSchema, TaskResponse
from typing import Generator

router = APIRouter()


# Dependencia para la sesión de la BD
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 📌 Obtener todas las tareas
@router.get("/", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)) -> list[TaskResponse]:
    tasks = TaskService.get_all_tasks(db)
    return [TaskResponse(**task.__dict__) for task in tasks]


# 📌 Crear una nueva tarea
@router.post("/", response_model=TaskResponse)
def create_task(task: TaskSchema, db: Session = Depends(get_db)) -> TaskResponse:
    return TaskService.create_task(db, task)


# 📌 Obtener una tarea por ID
@router.get("/{task_id}/", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)) -> TaskResponse:
    task = TaskService.get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# 📌 Actualizar una tarea por ID
@router.put("/{task_id}/", response_model=TaskResponse)
def update_task(
    task_id: int, updated_task: TaskSchema, db: Session = Depends(get_db)
) -> TaskResponse:
    task = TaskService.update_task(db, task_id, updated_task)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# 📌 Eliminar una tarea por ID
@router.delete("/{task_id}/")
def delete_task(task_id: int, db: Session = Depends(get_db)) -> dict:
    if not TaskService.delete_task(db, task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}
