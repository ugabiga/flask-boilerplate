from app.data.sql.models.user import User
from app.extensions.database import sql_session
from core.entities.users import User as UserEntity
from core.repositories.users import UserRepository


class UserSQLRepository(UserRepository):
    def create_user(self, nickname: str) -> UserEntity:
        new_user = User()
        new_user.nickname = nickname

        sql_session.add(new_user)
        sql_session.commit()

        return new_user.to_entity()
