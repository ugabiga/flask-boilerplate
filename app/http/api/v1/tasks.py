from typing import Tuple

from flasgger import swag_from
from flask import jsonify, request
from flask.wrappers import Response

from app.http.api import api
from app.http.api.v1 import version_prefix
from app.http.requests.v1 import task_request
from app.http.responses import build_response
from app.http.responses.tasks import TaskSchema
from core.use_cases.create_tasks import CreateTaskUseCase
from core.use_cases.get_tasks import GetTasksByUserUseCase

route_name = "tasks"


@swag_from("./task_index.yml")
@api.route(f"{version_prefix}/{route_name}")
def index() -> Tuple[Response, int]:
    req = task_request.GetUerTasksRequest(
        previous_id=request.args.get("previous_id"), limit=request.args.get("limit")
    )
    output = GetTasksByUserUseCase().execute(req.to_dto())
    return build_response(output, TaskSchema, True)


@api.route(f"{version_prefix}/{route_name}/<int:task_id>")
def detail(task_id):
    return jsonify({"result": True})


@api.route(f"{version_prefix}/{route_name}", methods=["POST"])
def create():
    req = task_request.CreateTaskRequest.from_dict(request.get_json())
    output = CreateTaskUseCase().execute(req.to_dto())
    return build_response(output, TaskSchema)


@api.route(f"{version_prefix}/{route_name}", methods=["PUT"])
def update():
    return jsonify({"result": True})


@api.route(f"{version_prefix}/{route_name}", methods=["DELETE"])
def delete():
    return jsonify({"result": True})
