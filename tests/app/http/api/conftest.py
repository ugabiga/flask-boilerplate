import pytest
from sqlalchemy.orm import scoped_session  # type:ignore

from app.data.sql.repositories.task import TaskSQLRepository


# noinspection PyUnusedLocal
@pytest.fixture(scope="function")
def task_repo(session: scoped_session) -> TaskSQLRepository:
    return TaskSQLRepository()
