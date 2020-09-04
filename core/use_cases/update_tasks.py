from dataclasses import dataclass

from core.entities.tasks import Task
from core.exceptions import NotAuthorizedError, NotFoundError
from core.repositories.tasks import TaskRepository
from core.use_case_outputs import Failure, Output, Success


@dataclass
class UpdateTaskDto:
    task_id: int
    user_id: int
    title: str
    contents: str

    def to_entity(self) -> Task:
        return Task(
            id=self.task_id,
            user_id=self.user_id,
            title=self.title,
            contents=self.contents,
        )


class UpdateTaskUseCase:
    def __init__(self, task_repository: TaskRepository) -> None:
        self.task_repository = task_repository

    def execute(self, dto: UpdateTaskDto) -> Output[Task]:
        try:
            self._check_task_authorization(dto)
        except NotFoundError:
            return Failure.build_not_found_error()
        except NotAuthorizedError:
            return Failure.build_not_authorized_error()

        try:
            new_task = self._update_task(dto)
        except NotFoundError:
            return Failure.build_not_found_error()

        return Success(new_task)

    def _check_task_authorization(self, dto: UpdateTaskDto) -> bool:
        task = self.task_repository.read_task(dto.task_id)

        if task is None:
            raise NotFoundError()

        if task.user_id != dto.user_id:
            raise NotAuthorizedError()

        return True

    def _update_task(self, dto: UpdateTaskDto) -> Task:
        entity = dto.to_entity()
        new_task = self.task_repository.update_task(
            entity.id, entity.title, entity.contents
        )

        if new_task is None:
            raise NotFoundError()

        return new_task
