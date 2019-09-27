from app.core.repositories.tasks import TaskRepository
from app.core.use_cases import BaseUseCase
from app.http.requests.v1.tasks import CreateTaskRequest


class CreateTaskUseCase(BaseUseCase):
    def __init__(self, task_repository: TaskRepository):
        self.repository = task_repository

    def execute(self, request: CreateTaskRequest):
        task = self.repository.create_task(
            request.user_id, request.title, request.contents
        )
        return task
