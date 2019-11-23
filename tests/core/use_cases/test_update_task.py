from unittest import mock

from app.core.entities.tasks import Task
from app.core.use_cases.tasks import CreateTaskUseCase
from app.core.use_cases.tasks import GetAllTasksUseCase
from app.http.requests.v1.tasks import CreateTaskRequest
from app.http.requests.v1.tasks import GetAllTasksRequest

