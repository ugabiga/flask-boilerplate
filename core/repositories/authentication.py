from abc import ABC
from typing import Optional

from core.entities.authentication import Authentication as AuthenticationEntity


class AuthenticationRepository(ABC):
    def create_auth(self, auth: AuthenticationEntity) -> AuthenticationEntity:
        raise NotImplementedError()

    def find_auth(
        self, category: str, identification: str, secret: str
    ) -> Optional[AuthenticationEntity]:
        raise NotImplementedError()
