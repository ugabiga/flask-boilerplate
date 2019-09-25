import pytest

from app.data.sql.repositories.tasks import TaskSQLRepository


from flask.app import Flask
@pytest.fixture(scope="function")
def repo(app: Flask) -> TaskSQLRepository:
    return TaskSQLRepository()
