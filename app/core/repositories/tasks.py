from abc import ABC
from typing import List
from typing import Optional

from app.core.dtos.tasks import UpdateTaskDto
from app.core.entities.tasks import Task


class TaskRepository(ABC):
    def create_task(self, user_id: int, title: str, contents: str) -> Task:
        raise NotImplementedError()

    def read_tasks(self, previous_id: int, limit: int) -> List[Task]:
        raise NotImplementedError()

    def update_task(self, dto: UpdateTaskDto) -> Optional[Task]:
        raise NotImplementedError()
