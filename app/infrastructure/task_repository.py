from sqlalchemy.orm import Session
from app.domain.task import Task
from app.schemas.task_schema import TaskSchema
from typing import Optional, Sequence


class TaskRepository:
    @staticmethod
    def get_all(db: Session) -> Sequence[Task]:
        tasks = db.query(Task).all()
        return list(tasks)

    @staticmethod
    def get_by_id(db: Session, task_id: int) -> Optional[Task]:
        task = db.query(Task).filter(Task.id == task_id).first()
        return task if isinstance(task, Task) else None

    @staticmethod
    def create(db: Session, task_data: TaskSchema) -> Task:
        task = Task(**task_data.dict())
        db.add(task)
        db.commit()
        db.refresh(task)
        return task

    @staticmethod
    def update(db: Session, task_id: int, task_data: TaskSchema) -> Optional[Task]:
        task = db.query(Task).filter(Task.id == task_id).first()
        if isinstance(task, Task):
            for key, value in task_data.dict().items():
                setattr(task, key, value)
            db.commit()
            db.refresh(task)
            return task
        return None

    @staticmethod
    def delete(db: Session, task_id: int) -> Optional[Task]:
        task = db.query(Task).filter(Task.id == task_id).first()
        if isinstance(task, Task):
            db.delete(task)
            db.commit()
            return task
        return None
