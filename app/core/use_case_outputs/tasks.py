from typing import Any
from typing import Dict
from typing import List

from app.core.entities.tasks import Task
from app.core.use_case_outputs import BaseUseCaseSuccessOutput


class CreateTaskUseCaseSuccessOutput(BaseUseCaseSuccessOutput):
    def __init__(self, task: Task) -> None:
        self.task = task

    def get_data(self) -> Task:
        return self.task

    def get_meta(self) -> Any:
        return None


class GetAllTasksUseCaseSuccessOutput(BaseUseCaseSuccessOutput):
    def __init__(self, tasks: List[Task], meta: Dict[str, int]) -> None:
        self.meta = meta
        self.tasks = tasks

    def get_data(self) -> List[Task]:
        return self.tasks

    def get_meta(self) -> Dict[str, int]:
        return self.meta


class UpdateTaskUseCaseSuccessOutput(BaseUseCaseSuccessOutput):
    def __init__(self, task: Task) -> None:
        self.task = task

    def get_data(self) -> Task:
        return self.task

    def get_meta(self) -> Any:
        return None
