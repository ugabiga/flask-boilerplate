from flask import request

from app.core.repositories.tasks import TaskRepository
from app.core.use_cases.create_task import CreateTaskUseCase
from app.extensions.injection import container
from app.http.api import api
from app.http.requests.v1.tasks import CreateTaskRequest
from app.http.responses import build_failure_response
from app.http.responses.tasks import build_create_task_success_response


@api.route("/v1/tasks")
def index():
    pass


@api.route("/v1/tasks", methods=["POST"])
def create():
    create_task_request = CreateTaskRequest.from_dict(request.get_json())
    output = CreateTaskUseCase(
        task_repository=container.get(TaskRepository), request=create_task_request
    ).execute()

    if output is False:
        return build_failure_response(output)

    return build_create_task_success_response(output)


@api.route("/v1/tasks", methods=["PUT"])
def edit():
    pass


@api.route("/v1/tasks", methods=["DELETE"])
def delete():
    pass
