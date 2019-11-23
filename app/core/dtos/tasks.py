from dataclasses import dataclass
from typing import Optional


@dataclass
class UpdateTaskDto:
    task_id: int
    title: Optional[str] = None
    contents: Optional[str] = None
