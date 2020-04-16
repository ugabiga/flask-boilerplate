from dataclasses import dataclass
from typing import Any, Optional, Union

from core.entities.tasks import Task
from core.exceptions import NotAuthorizedException, NotFoundException
from core.repositories.tasks import TaskRepository
from core.use_case_outputs import BaseUseCaseSuccessOutput, UseCaseFailureOutput


@dataclass
class UpdateTaskDto:
    task_id: int
    user_id: int
    title: Optional[str] = None
    contents: Optional[str] = None

    def to_entity(self) -> Task:
        return Task(id=self.task_id, title=self.title, contents=self.contents)


class UpdateTaskUseCaseOutput(BaseUseCaseSuccessOutput):
    def __init__(self, task: Task) -> None:
        self.task = task

    def get_data(self) -> Task:
        return self.task

    def get_meta(self) -> Any:
        return None


class UpdateTaskUseCase:
    def __init__(self, task_repository: TaskRepository) -> None:
        self.task_repository = task_repository

    def execute(
        self, dto: UpdateTaskDto
    ) -> Union[UpdateTaskUseCaseOutput, UseCaseFailureOutput]:
        try:
            self._check_task_authorization(dto)
        except NotFoundException:
            return UseCaseFailureOutput.build_not_found_error("task_not_found")
        except NotAuthorizedException:
            return UseCaseFailureOutput.build_not_authorized_error(
                "not_authorized_action"
            )

        try:
            new_task = self._update_task(dto)
        except NotFoundException:
            return UseCaseFailureOutput.build_not_found_error("task_not_found")

        return UpdateTaskUseCaseOutput(new_task)

    def _check_task_authorization(self, dto: UpdateTaskDto) -> bool:
        task = self.task_repository.read_task(dto.task_id)

        if task is None:
            raise NotFoundException()

        if task.user_id != dto.user_id:
            raise NotAuthorizedException()

        return True

    def _update_task(self, entity: UpdateTaskDto) -> Task:
        new_task = self.task_repository.update_task(entity.to_entity())

        if new_task is None:
            raise NotFoundException()

        return new_task
