from typing import Union

from app.core.repositories.tasks import TaskRepository
from app.core.use_case_outputs import UseCaseFailureOutput
from app.core.use_case_outputs import UseCaseFailureOutput
from app.core.use_case_outputs.tasks import CreateTaskUseCaseSuccessOutput
from app.core.use_case_outputs.tasks import CreateTaskUseCaseSuccessOutput
from app.core.use_cases import BaseUseCase
from app.http.requests.v1.tasks import CreateTaskRequest


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