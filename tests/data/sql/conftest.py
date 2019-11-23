from flask.app import Flask
import pytest

from app.core.repositories.tasks import TaskRepository
from app.data.sql.repositories.tasks import TaskSQLRepository
from app.extensions.injection import container


@pytest.fixture(scope="function")
def repo(app: Flask) -> TaskSQLRepository:
    return container.get(TaskRepository)
