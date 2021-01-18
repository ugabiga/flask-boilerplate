from app.http.api import api
from app.http.api.v1 import version_prefix
from app.http.requests import validate_request
from app.http.responses import build_response
from core.use_cases.authentications.create_token import (
    CreateTokenDto,
    CreateTokenUseCase,
)

route_name = "authentications"


@api.route(f"{version_prefix}/{route_name}", methods=["POST"])
@validate_request(CreateTokenDto)
def create_token(dto: CreateTokenDto):
    return build_response(CreateTokenUseCase().execute(dto))
