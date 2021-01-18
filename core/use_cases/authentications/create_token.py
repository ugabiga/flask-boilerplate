import inject
import jwt

from core.dtos.base import BaseDto
from core.helpers.encrypt import EncryptHelper
from core.repositories.authentication import AuthenticationRepository
from core.use_cases.output import Failure, Output, Success


class CreateTokenDto(BaseDto):
    category: str
    identification: str
    secret: str

    class Config:
        arbitrary_types_allowed = True


class CreateTokenUseCase:
    @inject.autoparams()
    def __init__(self, repository: AuthenticationRepository) -> None:
        self.__repository = repository
        self.__encrypt_helper = EncryptHelper()

    def execute(self, dto: CreateTokenDto) -> Output[str]:
        authentication = self.__repository.find_auth(dto.category, dto.identification)

        if authentication is None:
            return Failure.build_not_found_error()

        if authentication.secret != self.__encrypt_helper.encode(dto.secret):
            return Failure.build_not_authorized_error()

        return Success(self.__create_token(authentication.user_id))

    def __create_token(self, user_id: int):
        key = ""
        payload = {"user_id": user_id}

        byte_token = jwt.encode(payload=payload, key=key, algorithm="HS256")
        return byte_token.decode("UTF-8")
