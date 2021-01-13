from typing import Optional

from app.extensions.sql_client import SQLClient
from core.entities.users import User as UserEntity
from core.models.user import UserModel


class UserRepository:
    def create_user(self, nickname: str) -> UserEntity:
        new_user = UserModel()
        new_user.nickname = nickname

        user = SQLClient(new_user).create()

        return user.to_entity()

    def read_task(self, user_id: int) -> Optional[UserEntity]:
        user = SQLClient(UserModel).filter(UserModel.id == user_id).one_or_none()

        if user is None:
            return None

        return user.to_entity()
