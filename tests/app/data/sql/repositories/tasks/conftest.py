from flask.app import Flask
import pytest
from sqlalchemy.orm import scoped_session

from app.data.sql.repositories.task import TaskSQLRepository


# noinspection PyUnusedLocal
@pytest.fixture(scope="function")
def repo(app: Flask, session: scoped_session) -> TaskSQLRepository:
    return TaskSQLRepository()
