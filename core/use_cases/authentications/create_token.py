import inject
import jwt

from core.repositories.authentication import AuthenticationRepository
from core.use_case_outputs import Failure, Output, Success


class CreateTokenUseCase:
    @inject.autoparams()
    def __init__(self, repository: AuthenticationRepository) -> None:
        self.__repository = repository

    def execute(self, category: str, identification: str, secret: str) -> Output[str]:
        authentication = self.__repository.find_auth(category, identification)

        if authentication is None:
            return Failure.build_not_found_error()

        if authentication.secret != secret:
            return Failure.build_not_authorized_error()

        return Success(self.__create_token(authentication.user_id))

    def __create_token(self, user_id: int):
        key = ""
        payload = {"user_id": user_id}

        byte_token = jwt.encode(payload=payload, key=key, algorithm="HS256")
        return byte_token.decode("UTF-8")
