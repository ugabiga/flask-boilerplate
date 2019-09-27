from flask import request

from app.core.repositories.tasks import TaskRepository
from app.core.use_cases.tasks import CreateTaskUseCase
from app.extensions.injection import container
from app.http.api import api
from app.http.requests.v1.tasks import CreateTaskRequest


@api.route("/v1/tasks")
def index():
    pass


@api.route("/v1/tasks", methods=["POST"])
def create():
    payload = request.get_json()
    create_todo_request = CreateTaskRequest.from_dict(payload)
    uc = CreateTaskUseCase(task_repository=container.get(TaskRepository))
    uc_result = uc.execute(request=create_todo_request)
    # TODO : Add response


@api.route("/v1/tasks", methods=["PUT"])
def edit():
    pass


@api.route("/v1/tasks", methods=["DELETE"])
def delete():
    pass
