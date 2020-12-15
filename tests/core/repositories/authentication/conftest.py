import pytest
from sqlalchemy.orm import scoped_session  # type:ignore

from core.repositories.authentication import AuthenticationRepository


# noinspection PyUnusedLocal
@pytest.fixture(scope="function")
def repo(session: scoped_session) -> AuthenticationRepository:
    return AuthenticationRepository()
