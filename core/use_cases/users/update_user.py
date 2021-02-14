import inject

from core.dtos.base import BaseDto
from core.repositories.users import UserRepository
from core.use_cases.output import Output, Success


class UpdateUserDto(BaseDto):
    user_id: int
    nickname: str


class UpdateUserUseCase:
    @inject.autoparams()
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repo = user_repository

    def execute(self, dto: UpdateUserDto) -> Output[dict]:
        self.user_repo.update_user(user_id=dto.user_id, nickname=dto.nickname)
        return Success({})
