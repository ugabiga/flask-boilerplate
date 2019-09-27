from flask import jsonify
from flask import request

from app.core.entities.tasks import Task
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
    create_todo_request = CreateTaskRequest.from_dict(request.get_json())
    result = CreateTaskUseCase(
        task_repository=container.get(TaskRepository), request=create_todo_request
    ).execute()

    if result is False:
        return result.build_response()

    return jsonify(data=result.get_data()), 200


@api.route("/v1/tasks", methods=["PUT"])
def edit():
    pass


@api.route("/v1/tasks", methods=["DELETE"])
def delete():
    pass
