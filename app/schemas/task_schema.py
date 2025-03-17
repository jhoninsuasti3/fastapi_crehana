from pydantic import BaseModel
from typing import Optional

class TaskSchema(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TaskResponse(TaskSchema):
    id: int
