from abc import ABC

from core.entities.users import User


class UserRepository(ABC):
    def create_user(self, nickname) -> User:
        raise NotImplementedError()
