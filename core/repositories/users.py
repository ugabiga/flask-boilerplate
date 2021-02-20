from typing import Optional

from core.entities.users import User as UserEntity
from core.extensions import rdb
from core.models.user import UserModel


class UserRepository:
    def create_user(self, nickname: str) -> UserEntity:
        new_user = UserModel()
        new_user.nickname = nickname

        user = rdb.Query(new_user).create()

        return user.to_entity()

    def update_user(self, user_id: int, nickname: str):
        rdb.Query(UserModel).filter(UserModel.id == user_id).update(
            {"nickname": nickname}
        )

    def get_user(self, user_id: int) -> Optional[UserEntity]:
        user = rdb.Query(UserModel).filter(UserModel.id == user_id).one_or_none()

        if user is None:
            return None

        return user.to_entity()
