from abc import ABC
from typing import List

from app.core.entities.tasks import Task


class TaskRepository(ABC):
    def create_task(self, user_id: int, title: str, contents: str) -> Task:
        raise NotImplementedError()

    def get(self, previous_id: int, limit: int) -> List[Task]:
        raise NotImplementedError()
