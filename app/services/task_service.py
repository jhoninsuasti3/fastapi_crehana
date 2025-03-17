from sqlalchemy.orm import Session
from app.infrastructure.task_repository import TaskRepository
from app.schemas.task_schema import TaskSchema
from app.domain.task import Task
from typing import Optional, Sequence


class TaskService:
    @staticmethod
    def get_all_tasks(db: Session) -> Sequence[Task]:  # ✅ Retorna lista de tareas
        return TaskRepository.get_all(db)

    @staticmethod
    def create_task(db: Session, task_data: TaskSchema) -> Task:  # ✅ Retorna una tarea
        return TaskRepository.create(db, task_data)

    @staticmethod
    def get_task_by_id(db: Session, task_id: int) -> Optional[Task]:  # ✅ Puede retornar None
        return TaskRepository.get_by_id(db, task_id)

    @staticmethod
    def update_task(db: Session, task_id: int, updated_task: TaskSchema) -> Optional[Task]:
        return TaskRepository.update(db, task_id, updated_task)

    @staticmethod
    def delete_task(db: Session, task_id: int) -> Optional[Task]:
        return TaskRepository.delete(db, task_id)
