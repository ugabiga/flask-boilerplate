from typing import Optional

from app.extensions.database import session
from core.entities.users import User as UserEntity
from core.models.user import UserModel


class UserRepository:
    def create_user(self, nickname: str) -> UserEntity:
        new_user = UserModel()
        new_user.nickname = nickname

        session.add(new_user)
        session.commit()

        return new_user.to_entity()

    def read_task(self, user_id: int) -> Optional[UserEntity]:
        user: UserModel = session.query(UserModel).filter(UserModel.id == user_id).one_or_none()

        if user is None:
            return None

        return user.to_entity()
