from abc import ABC
from abc import abstractmethod

from app.http.requests.v1.tasks import CreateTaskRequest


class BaseUseCase(ABC):
    @abstractmethod
    def execute(self, request: CreateTaskRequest):
        raise NotImplementedError()
