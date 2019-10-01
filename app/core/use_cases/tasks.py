from typing import Union

from app.core.repositories.tasks import TaskRepository
from app.core.use_case_outputs import UseCaseFailureOutput
from app.core.use_case_outputs.tasks import CreateTaskUseCaseSuccessOutput
from app.core.use_case_outputs.tasks import GetAllTasksUseCaseSuccessOutput
from app.core.use_cases import BaseUseCase
from app.http.requests.v1.tasks import CreateTaskRequest
from app.http.requests.v1.tasks import GetAllTasksRequest


class CreateTaskUseCase(BaseUseCase):
    def __init__(
        self, task_repository: TaskRepository, request: CreateTaskRequest
    ) -> None:
        self.request = request
        self.repository = task_repository

    def execute(self) -> Union[CreateTaskUseCaseSuccessOutput, UseCaseFailureOutput]:
        task = self.repository.create_task(
            self.request.user_id, self.request.title, self.request.contents
        )

        if not task:
            return UseCaseFailureOutput.build_not_found_error("task_not_found")

        return CreateTaskUseCaseSuccessOutput(task)


class GetAllTasksUseCase(BaseUseCase):
    def __init__(
        self, task_repository: TaskRepository, request: GetAllTasksRequest
    ) -> None:
        self.request = request
        self.task_repository = task_repository

    def execute(self) -> Union[GetAllTasksUseCaseSuccessOutput, UseCaseFailureOutput]:
        tasks = self.task_repository.get(
            previous_id=self.request.previous_id, limit=self.request.limit
        )

        if len(tasks) < 1:
            return UseCaseFailureOutput.build_not_found_error("tasks_not_found")

        return GetAllTasksUseCaseSuccessOutput(
            tasks=tasks, meta={"previous_id": tasks[-1].id, "limit": self.request.limit}
        )
