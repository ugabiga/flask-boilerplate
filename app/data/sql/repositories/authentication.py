import hashlib

from app.core.entities.authentication import Authentication as AuthenticationEntity
from app.core.repositories.authentication import AuthenticationRepository
from app.data.sql.models.authentication import Authentication
from app.extensions.database import sql_session


class AuthenticationSQLRepository(AuthenticationRepository):
    def create_auth(self, auth: AuthenticationEntity) -> AuthenticationEntity:
        new_auth = Authentication(
            user_id=auth.user_id,
            category=auth.category,
            identification=auth.identification,
            secret=auth.secret,
        )
        sql_session.add(new_auth)
        sql_session.commit()

        return new_auth.to_entity()

    def _encoding_secret(self, category: str, secret: str) -> str:
        salt = "secret"

        if category == AuthenticationEntity.EMAIL:
            return hashlib.sha512(secret + salt).hexdigest()
