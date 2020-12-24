from typing import Optional

from app.extensions.database import session
from core.entities.users import User as UserEntity
from core.models.user import User


class UserRepository:
    def create_user(self, nickname: str) -> UserEntity:
        new_user = User()
        new_user.nickname = nickname

        session.add(new_user)
        session.commit()

        return new_user.to_entity()

    def read_task(self, user_id: int) -> Optional[UserEntity]:
        user: User = session.query(User).filter(User.id == user_id).one_or_none()

        if user is None:
            return None

        return user.to_entity()
