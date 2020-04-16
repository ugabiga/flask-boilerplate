from flasgger import swag_from
from flask import jsonify, request

from app.http.api import api
from app.http.api.v1 import version_prefix
from app.http.requests.v1.users import CreateUserRequest
from app.http.responses import build_success_dump_response
from app.http.responses.users import UserSchema
from core.use_cases.create_users import CreateUserUseCase

route_name = "users"


@swag_from("")
@api.route(f"{version_prefix}/{route_name}")
def index():
    return jsonify({"result": True})


@swag_from("")
@api.route(f"{version_prefix}/{route_name}", methods=["POST"])
def create():
    dto = CreateUserRequest.from_dict(request.get_json()).to_dto()
    output = CreateUserUseCase().execute(dto)
    return build_success_dump_response(UserSchema, output.get_data())


@swag_from("")
@api.route(f"{version_prefix}/{route_name}", methods=["PUT"])
def update():
    return jsonify({"result": True})


@swag_from("")
@api.route(f"{version_prefix}/{route_name}", methods=["DELETE"])
def delete():
    return jsonify({"result": True})
