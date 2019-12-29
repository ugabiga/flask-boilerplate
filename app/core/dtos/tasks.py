from dataclasses import dataclass
from typing import Optional


@dataclass
class UpdateTaskDto:
    task_id: int
    title: Optional[str] = None
    contents: Optional[str] = None


@dataclass
class CreateTaskDto:
    user_id: int
    title: str
    contents: str


@dataclass
class GetUserTasksDto:
    user_id: int
    previous_id: int = 0
    limit: int = 10
