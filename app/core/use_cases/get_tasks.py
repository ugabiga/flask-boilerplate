from dataclasses import dataclass
from typing import Dict
from typing import List
from typing import Union

from app.core.entities.tasks import Task
from app.core.repositories.tasks import TaskRepository
from app.core.use_case_outputs import BaseUseCaseSuccessOutput
from app.core.use_case_outputs import UseCaseFailureOutput
from app.core.use_cases import BaseUseCase


@dataclass
class GetUserTasksDto:
    user_id: int
    previous_id: int = 0
    limit: int = 10


class GetUserTasksUseCaseOutput(BaseUseCaseSuccessOutput):
    def __init__(self, tasks: List[Task], meta: Dict[str, int]) -> None:
        self.meta = meta
        self.tasks = tasks

    def get_data(self) -> List[Task]:
        return self.tasks

    def get_meta(self) -> Dict[str, int]:
        return self.meta


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
