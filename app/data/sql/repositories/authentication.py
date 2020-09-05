import hashlib
from typing import Optional

from app.data.sql.models.authentication import Authentication
from app.extensions.database import sql_session
from core.entities.authentication import Authentication as AuthenticationEntity
from core.repositories.authentication import AuthenticationRepository


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

    def _encoding_secret(self, secret: str) -> str:
        salt = "secret"

        return hashlib.sha512((secret + salt).encode("utf-8")).hexdigest()

    def find_auth(
        self, category: str, identification: str, secret: str
    ) -> Optional[AuthenticationEntity]:
        authentication = (
            sql_session.query(Authentication)
            .filter(Authentication.identification == identification)
            .filter(Authentication.category == category)
            .one_or_none()
        )

        return None if authentication is None else authentication.to_entity()
