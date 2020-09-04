import inject

from core.dto import BaseDto
from core.entities.authentication import Authentication
from core.entities.users import User
from core.repositories.authentication import AuthenticationRepository
from core.repositories.users import UserRepository
from core.use_case_outputs import Output, Success


class CreateUserDto(BaseDto):
    nickname: str
    auth_category: str
    auth_identification: str
    auth_secret: str


class CreateUserUseCase:
    @inject.autoparams()
    def __init__(
        self, user_repository: UserRepository, auth_repository: AuthenticationRepository
    ) -> None:
        self.user_repo = user_repository
        self.auth_repo = auth_repository

    def execute(self, dto: CreateUserDto) -> Output[User]:
        user = self.user_repo.create_user(dto.nickname)
        auth = self._create_authentication(user.id, dto)
        user.authentications.append(auth)

        return Success(user)

    def _create_authentication(
        self, user_id: int, dto: CreateUserDto
    ) -> Authentication:
        return self.auth_repo.create_auth(
            Authentication(
                user_id=user_id,
                category=dto.auth_category,
                identification=dto.auth_identification,
                secret=dto.auth_secret,
            )
        )
