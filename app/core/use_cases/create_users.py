from typing import Any

from app.core.dtos.users import CreateUserDto
from app.core.repositories.users import UserRepository
from app.core.use_cases import BaseUseCase


class CreateUserUseCase(BaseUseCase):
    def __init__(self, user_repository: UserRepository, dto: CreateUserDto):
        self.dto = dto
        self.repo = user_repository

    def execute(self) -> Any:
        return self.repo.create_user(self.dto.nickname)
