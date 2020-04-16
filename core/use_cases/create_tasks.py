from dataclasses import dataclass
from typing import Any
from typing import Union

from core.entities.tasks import Task
from core.repositories.tasks import TaskRepository
from core.use_case_outputs import BaseUseCaseSuccessOutput
from core.use_case_outputs import UseCaseFailureOutput
from core.use_cases import BaseUseCase


@dataclass
class CreateTaskDto:
    user_id: int
    title: str
    contents: str


class CreateTaskUseCaseOutput(BaseUseCaseSuccessOutput):
    def __init__(self, task: Task) -> None:
        self.task = task

    def get_data(self) -> Task:
        return self.task

    def get_meta(self) -> Any:
        return None


class CreateTaskUseCase(BaseUseCase):
    def __init__(self, task_repository: TaskRepository, dto: CreateTaskDto) -> None:
        self.dto = dto
        self.repository = task_repository

    def execute(self) -> Union[CreateTaskUseCaseOutput, UseCaseFailureOutput]:
        task = self.repository.create_task(
            self.dto.user_id, self.dto.title, self.dto.contents
        )

        if not task:
            return UseCaseFailureOutput.build_not_found_error("task_not_found")

        return CreateTaskUseCaseOutput(task)
