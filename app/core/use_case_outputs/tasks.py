from app.core.entities.tasks import Task
from app.core.entities.tasks import Task
from app.core.use_case_outputs import BaseUseCaseSuccessOutput


class CreateTaskUseCaseSuccessOutput(BaseUseCaseSuccessOutput):
    def __init__(self, task: Task):
        self.task = task

    def get_data(self) -> Task:
        return self.task
