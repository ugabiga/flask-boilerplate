import pytest
from flask.app import Flask
from sqlalchemy.orm import scoped_session

from app.data.sql.repositories.users import UserSQLRepository


# noinspection PyUnusedLocal
@pytest.fixture(scope="function")
def repo(app: Flask, session: scoped_session) -> UserSQLRepository:
    return UserSQLRepository()
