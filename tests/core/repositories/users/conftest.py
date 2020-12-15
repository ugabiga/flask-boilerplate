import pytest
from sqlalchemy.orm.scoping import scoped_session  # type:ignore

from core.repositories.users import UserRepository


# noinspection PyUnusedLocal
@pytest.fixture(scope="function")
def repo(session: scoped_session) -> UserRepository:
    return UserRepository()
