from app.extensions.database import sql_session
from core.entities.users import User as UserEntity
from core.models.user import User


class UserRepository:
    def create_user(self, nickname: str) -> UserEntity:
        new_user = User()
        new_user.nickname = nickname

        sql_session.add(new_user)
        sql_session.commit()

        return new_user.to_entity()
