import pytest
from sqlalchemy.orm import scoped_session

from app.data.sql.repositories.authentication import AuthenticationSQLRepository


# noinspection PyUnusedLocal
@pytest.fixture(scope="function")
def repo(session: scoped_session) -> AuthenticationSQLRepository:
    return AuthenticationSQLRepository()
