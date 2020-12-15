from flasgger import swag_from
from flask import jsonify, request

from app.http.api import api
from app.http.api.v1 import version_prefix
from app.http.responses import build_response
from app.http.responses.users import UserSchema
from core.use_cases.users.create_users import CreateUserDto, CreateUserUseCase

route_name = "users"


@swag_from("")
@api.route(f"{version_prefix}/{route_name}")
def index():
    return jsonify({"result": True})


@swag_from("")
@api.route(f"{version_prefix}/{route_name}", methods=["POST"])
def create():
    dto = CreateUserDto.validate_from_dict(request.get_json())
    output = CreateUserUseCase().execute(dto)
    return build_response(output, UserSchema)


@swag_from("")
@api.route(f"{version_prefix}/{route_name}", methods=["PUT"])
def update():
    return jsonify({"result": True})


@swag_from("")
@api.route(f"{version_prefix}/{route_name}", methods=["DELETE"])
def delete():
    return jsonify({"result": True})
