from flask import request

from app.core.repositories.tasks import TaskRepository
from app.core.use_cases.create_tasks import CreateTaskUseCase
from app.extensions.injection import container
from app.http.api import api
from app.http.requests.v1.tasks import CreateTaskRequest
from app.http.responses import build_failure_response
from app.http.responses.tasks import build_create_task_success_response

task_repository = container.get(TaskRepository)
version_prefix = "/v1"


@api.route(f"{version_prefix}/tasks")
def index():
    pass


@api.route(f"{version_prefix}/tasks", methods=["POST"])
def create():
    task_request = CreateTaskRequest.from_dict(request.get_json())
    output = CreateTaskUseCase(
        task_repository=task_repository, dto=task_request.to_dto()
    ).execute()

    if output is False:
        return build_failure_response(output)

    return build_create_task_success_response(output)


@api.route(f"{version_prefix}/tasks", methods=["PUT"])
def update():
    pass


@api.route(f"{version_prefix}/tasks", methods=["DELETE"])
def delete():
    pass
