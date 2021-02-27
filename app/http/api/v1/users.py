from flasgger import swag_from
from flask import jsonify

from app.extensions.swagger.builder import doc_build
from app.http.api import api, validate_request
from app.http.api.v1 import version_prefix
from app.http.responses import build_response
from app.http.responses.users import UserSchema
from core.use_cases.users.create_users import CreateUserDto, CreateUserUseCase

route_name = "users"


@api.route(f"{version_prefix}/{route_name}")
def index_user():
    return jsonify({"result": True})


@api.route(f"{version_prefix}/{route_name}", methods=["POST"])
@swag_from(doc_build("User", "user", "User"))
@validate_request(CreateUserDto)
def create_user(dto: CreateUserDto):
    """
    Create User
    """
    output = CreateUserUseCase().execute(dto)
    return build_response(output, UserSchema)


@api.route(f"{version_prefix}/{route_name}", methods=["PUT"])
def update_user():
    return jsonify({"result": True})


@api.route(f"{version_prefix}/{route_name}", methods=["DELETE"])
def delete_user():
    return jsonify({"result": True})
