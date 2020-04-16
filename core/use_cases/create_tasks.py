from dataclasses import dataclass
from typing import Any, Union

import inject

from core.entities.tasks import Task
from core.repositories.tasks import TaskRepository
from core.use_case_outputs import BaseUseCaseSuccessOutput, UseCaseFailureOutput


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


class CreateTaskUseCase:
    @inject.autoparams()
    def __init__(self, task_repository: TaskRepository) -> None:
        self.repository = task_repository

    def execute(
        self, dto: CreateTaskDto
    ) -> Union[CreateTaskUseCaseOutput, UseCaseFailureOutput]:
        task = self.repository.create_task(dto.user_id, dto.title, dto.contents)

        if not task:
            return UseCaseFailureOutput.build_not_found_error("task_not_found")

        return CreateTaskUseCaseOutput(task)
