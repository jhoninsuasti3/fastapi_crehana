from sqlalchemy.orm import Session
from app.infrastructure.task_repository import TaskRepository
from app.schemas.task_schema import TaskSchema

class TaskService:
    @staticmethod
    def get_all_tasks(db: Session):
        return TaskRepository.get_all(db)

    @staticmethod
    def create_task(db: Session, task_data: TaskSchema):
        return TaskRepository.create(db, task_data)
