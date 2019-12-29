from abc import ABC

from app.core.entities.users import User


class UserRepository(ABC):
    def create_user(self, nickname) -> User:
        raise NotImplementedError()
