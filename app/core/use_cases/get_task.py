from typing import Union

from app.core.dtos.tasks import GetUserTasksDto
from app.core.repositories.tasks import TaskRepository
from app.core.use_case_outputs import UseCaseFailureOutput
from app.core.use_case_outputs.tasks import GetUserTasksUseCaseOutput
from app.core.use_cases import BaseUseCase


class GetUserTasksUseCase(BaseUseCase):
    def __init__(self, task_repository: TaskRepository, dto: GetUserTasksDto) -> None:
        self.dto = dto
        self.task_repository = task_repository

    def execute(self) -> Union[GetUserTasksUseCaseOutput, UseCaseFailureOutput]:
        tasks = self.task_repository.get_tasks(
            previous_id=self.dto.previous_id, limit=self.dto.limit
        )

        if len(tasks) < 1:
            return UseCaseFailureOutput.build_not_found_error("tasks_not_found")

        return GetUserTasksUseCaseOutput(
            tasks=tasks, meta={"previous_id": tasks[-1].id, "limit": self.dto.limit}
        )
