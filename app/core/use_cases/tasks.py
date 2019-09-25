from app.core.repositories.tasks import TaskRepository
from app.core.use_cases import BaseUseCase
from app.http.requests.v1.tasks import CreateTaskRequest


class CreateTaskUseCase(BaseUseCase):
    def __init__(self, request: CreateTaskRequest, task_repository: TaskRepository):
        self.request = request
        self.repository = task_repository

    def execute(self):
        self.repository.create_task(
            self.request.user_id, self.request.title, self.request.contents
        )
