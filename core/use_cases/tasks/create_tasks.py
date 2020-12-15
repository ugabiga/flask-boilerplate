import inject

from core.dtos.base import BaseDto
from core.entities.tasks import Task
from core.repositories.tasks import TaskRepository
from core.use_cases.output import Failure, Output, Success


class CreateTaskDto(BaseDto):
    user_id: int
    title: str
    contents: str


class CreateTaskUseCase:
    @inject.autoparams()
    def __init__(self, task_repository: TaskRepository) -> None:
        self.repository = task_repository

    def execute(self, dto: CreateTaskDto) -> Output[Task]:
        task = self.repository.create_task(dto.user_id, dto.title, dto.contents)

        if not task:
            return Failure.build_not_found_error()

        return Success(task)
