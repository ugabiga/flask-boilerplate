import pytest
from sqlalchemy.orm import scoped_session  # type:ignore

from core.repositories.authentication import AuthenticationRepository
from core.repositories.tasks import TaskRepository
from core.repositories.users import UserRepository


# noinspection PyUnusedLocal
@pytest.fixture(scope="function")
def task_repo(session: scoped_session) -> TaskRepository:
    return TaskRepository()


# noinspection PyUnusedLocal
@pytest.fixture(scope="function")
def auth_repo(session: scoped_session) -> AuthenticationRepository:
    return AuthenticationRepository()


# noinspection PyUnusedLocal
@pytest.fixture(scope="function")
def user_repo(session: scoped_session) -> UserRepository:
    return UserRepository()
