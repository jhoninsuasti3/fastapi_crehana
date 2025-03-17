from sqlalchemy.orm import Session
from app.domain.task import Task
from app.schemas.task_schema import TaskSchema

class TaskRepository:
    @staticmethod
    def get_all(db: Session):
        return db.query(Task).all()

    @staticmethod
    def get_by_id(db: Session, task_id: int):
        return db.query(Task).filter(Task.id == task_id).first()

    @staticmethod
    def create(db: Session, task_data: TaskSchema):
        task = Task(**task_data.dict())
        db.add(task)
        db.commit()
        db.refresh(task)
        return task

    @staticmethod
    def update(db: Session, task_id: int, task_data: TaskSchema):
        task = db.query(Task).filter(Task.id == task_id).first()
        if task:
            for key, value in task_data.dict().items():
                setattr(task, key, value)
            db.commit()
            db.refresh(task)
        return task

    @staticmethod
    def delete(db: Session, task_id: int):
        task = db.query(Task).filter(Task.id == task_id).first()
        if task:
            db.delete(task)
            db.commit()
        return task
