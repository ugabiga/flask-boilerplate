from flask.app import Flask
import pytest
from sqlalchemy.orm import scoped_session

from app.core.repositories.tasks import TaskRepository
from app.data.sql.repositories.task import TaskSQLRepository
from app.extensions.injection import container


# noinspection PyUnusedLocal
@pytest.fixture(scope="function")
def repo(app: Flask, session: scoped_session) -> TaskSQLRepository:
    return container.get(TaskRepository)
