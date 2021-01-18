from flask import request

from app.http.api import api
from app.http.api.v1 import version_prefix
from app.http.responses import build_response
from core.use_cases.authentications.create_token import (
    CreateTokenDto,
    CreateTokenUseCase,
)

route_name = "authentications"


@api.route(f"{version_prefix}/{route_name}", methods=["POST"])
def create_token():
    dto = CreateTokenDto.validate_from_dict(request.get_json())
    output = CreateTokenUseCase().execute(dto)
    return build_response(output)
