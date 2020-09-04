import pytest
from sqlalchemy.orm.scoping import scoped_session  # type:ignore

from app.data.sql.repositories.task import TaskSQLRepository


# noinspection PyUnusedLocal
@pytest.fixture(scope="function")
def repo(session: scoped_session) -> TaskSQLRepository:
    return TaskSQLRepository()
