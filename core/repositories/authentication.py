from typing import Optional

from core.entities.authentication import Authentication as AuthenticationEntity
from core.extensions import rdb
from core.helpers.encrypt import EncryptHelper
from core.models.authentication import AuthenticationModel


class AuthenticationRepository:
    def create_auth(self, auth: AuthenticationEntity) -> AuthenticationEntity:
        new_auth: AuthenticationModel = AuthenticationModel(
            user_id=auth.user_id,
            category=auth.category,
            identification=auth.identification,
            secret=EncryptHelper().encode(auth.secret),
        )
        auth = rdb.Query(new_auth).create()

        return auth.to_entity()

    def find_auth(
        self, category: str, identification: str
    ) -> Optional[AuthenticationEntity]:
        authentication = (
            rdb.Query(AuthenticationModel)
            .filter(AuthenticationModel.identification == identification)
            .filter(AuthenticationModel.category == category)
            .one_or_none()
        )

        return None if authentication is None else authentication.to_entity()
