from dataclasses import dataclass
from typing import Any

from app.core.entities.users import User
from app.core.repositories.users import UserRepository
from app.core.use_case_outputs import BaseUseCaseSuccessOutput
from app.core.use_cases import BaseUseCase


@dataclass
class CreateUserDto:
    nickname: str


class CreateUserUseCaseOutput(BaseUseCaseSuccessOutput):
    def __init__(self, user: User) -> None:
        self.user = user

    def get_data(self) -> User:
        return self.user

    def get_meta(self) -> Any:
        return None


class CreateUserUseCase(BaseUseCase):
    def __init__(self, user_repository: UserRepository, dto: CreateUserDto) -> None:
        self.dto = dto
        self.repo = user_repository

    def execute(self) -> CreateUserUseCaseOutput:
        user = self.repo.create_user(self.dto.nickname)
        return CreateUserUseCaseOutput(user)
