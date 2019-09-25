from abc import ABC

from app.core.entities.tasks import Task


class TaskRepository(ABC):
    def create_task(self, user_id: int, title: str, contents: str) -> Task:
        raise NotImplementedError()
