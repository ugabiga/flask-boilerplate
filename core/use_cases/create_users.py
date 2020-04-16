from dataclasses import dataclass
from typing import Any

from core.entities.authentication import Authentication
from core.entities.users import User
from core.repositories.authentication import AuthenticationRepository
from core.repositories.users import UserRepository
from core.use_case_outputs import BaseUseCaseSuccessOutput
from core.use_cases import BaseUseCase


@dataclass
class CreateUserDto:
    nickname: str
    auth_category: str
    auth_identification: str
    auth_secret: str


class CreateUserUseCaseOutput(BaseUseCaseSuccessOutput):
    def __init__(self, user: User) -> None:
        self.user = user

    def get_data(self) -> User:
        return self.user

    def get_meta(self) -> Any:
        return None


class CreateUserUseCase(BaseUseCase):
    def __init__(
        self,
        user_repository: UserRepository,
        auth_repository: AuthenticationRepository,
        dto: CreateUserDto,
    ) -> None:
        self.dto = dto
        self.user_repo = user_repository
        self.auth_repo = auth_repository

    def execute(self) -> CreateUserUseCaseOutput:
        user = self.user_repo.create_user(self.dto.nickname)
        auth = self._create_authentication(user.id)
        user.authentications.append(auth)

        return CreateUserUseCaseOutput(user)

    def _create_authentication(self, user_id: int) -> Authentication:
        return self.auth_repo.create_auth(
            Authentication(
                user_id=user_id,
                category=self.dto.auth_category,
                identification=self.dto.auth_identification,
                secret=self.dto.auth_secret,
            )
        )
