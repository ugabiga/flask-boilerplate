from dataclasses import dataclass
from typing import Any

from app.core.repositories.users import UserRepository
from app.core.use_cases import BaseUseCase


@dataclass
class CreateUserDto:
    nickname: str


class CreateUserUseCase(BaseUseCase):
    def __init__(self, user_repository: UserRepository, dto: CreateUserDto) -> None:
        self.dto = dto
        self.repo = user_repository

    def execute(self) -> Any:
        return self.repo.create_user(self.dto.nickname)
