import pytest
from sqlalchemy.orm.scoping import scoped_session  # type:ignore

from core.repositories.tasks import TaskRepository


# noinspection PyUnusedLocal
@pytest.fixture(scope="function")
def repo(session: scoped_session) -> TaskRepository:
    return TaskRepository()
