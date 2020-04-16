from dataclasses import dataclass
from typing import Any
from typing import Optional
from typing import Union

from core.entities.tasks import Task
from core.exceptions import NotAuthorizedException
from core.exceptions import NotFoundException
from core.repositories.tasks import TaskRepository
from core.use_case_outputs import BaseUseCaseSuccessOutput
from core.use_case_outputs import UseCaseFailureOutput
from core.use_cases import BaseUseCase


@dataclass
class UpdateTaskDto:
    task_id: int
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


class UpdateTaskUseCase(BaseUseCase):
    def __init__(
        self, task_repository: TaskRepository, user_id: int, dto: UpdateTaskDto
    ) -> None:
        self.dto = dto
        self.user_id = user_id
        self.task_repository = task_repository

    def execute(self) -> Union[UpdateTaskUseCaseOutput, UseCaseFailureOutput]:
        dto = self.dto

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

        if task.user_id != self.user_id:
            raise NotAuthorizedException()

        return True

    def _update_task(self, entity: UpdateTaskDto) -> Task:
        new_task = self.task_repository.update_task(entity.to_entity())

        if new_task is None:
            raise NotFoundException()

        return new_task
