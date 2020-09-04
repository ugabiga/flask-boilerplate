from typing import Tuple

from flasgger import swag_from
from flask import jsonify, request
from flask.wrappers import Response

from app.http.api import api
from app.http.api.v1 import version_prefix
from app.http.responses import build_response
from app.http.responses.tasks import TaskSchema
from core.use_cases.create_tasks import CreateTaskDto, CreateTaskUseCase
from core.use_cases.get_tasks import GetTasksByUserUseCase, GetUserTasksDto

route_name = "tasks"


@swag_from("./task_index.yml")
@api.route(f"{version_prefix}/{route_name}")
def index() -> Tuple[Response, int]:
    request_dict: dict = request.args.to_dict()
    request_dict.update({"user_id": 1})
    dto = GetUserTasksDto.validate_from_dict(request_dict)
    output = GetTasksByUserUseCase().execute(dto)
    return build_response(output, TaskSchema, True)


@api.route(f"{version_prefix}/{route_name}/<int:task_id>")
def detail(task_id):
    return jsonify({"result": True})


@api.route(f"{version_prefix}/{route_name}", methods=["POST"])
def create():
    dto = CreateTaskDto.validate_from_dict(request.get_json())
    output = CreateTaskUseCase().execute(dto)
    return build_response(output, TaskSchema)


@api.route(f"{version_prefix}/{route_name}", methods=["PUT"])
def update():
    return jsonify({"result": True})


@api.route(f"{version_prefix}/{route_name}", methods=["DELETE"])
def delete():
    return jsonify({"result": True})
