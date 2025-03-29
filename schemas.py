from pydantic import BaseModel
from typing import Optional

class TaskBase (BaseModel):
    title : str
    description: Optional[str] = None
    status: Optional [str] = "pendiente"
    assignee:Optional[str] = None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id:int

    class Config:
        from_attributes = True

