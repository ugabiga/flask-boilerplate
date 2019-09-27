from typing import Union

from app.core.entities.tasks import Task
from app.core.repositories.tasks import TaskRepository
from app.core.use_case_output import BaseUseCaseSuccessOutput
from app.core.use_case_output import UseCaseFailureOutput
from app.core.use_cases import BaseUseCase
from app.http.requests.v1.tasks import CreateTaskRequest


class CreateTaskUseCase(BaseUseCase):
    class CreateTaskUseCaseSuccessOutput(BaseUseCaseSuccessOutput):
        def __init__(self, task: Task):
            self.task = task

        def get_data(self) -> Task:
            return self.task

    def __init__(self, task_repository: TaskRepository, request: CreateTaskRequest):
        self.request = request
        self.repository = task_repository

    def execute(self) -> Union[CreateTaskUseCaseSuccessOutput, UseCaseFailureOutput]:
        task = self.repository.create_task(
            self.request.user_id, self.request.title, self.request.contents
        )

        if not task:
            return UseCaseFailureOutput.build_not_found_error("task not found")

        return self.CreateTaskUseCaseSuccessOutput(task)
