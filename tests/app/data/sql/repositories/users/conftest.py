import pytest
from sqlalchemy.orm.scoping import scoped_session  # type:ignore

from app.data.sql.repositories.users import UserSQLRepository


# noinspection PyUnusedLocal
@pytest.fixture(scope="function")
def repo(session: scoped_session) -> UserSQLRepository:
    return UserSQLRepository()
