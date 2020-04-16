from flask.app import Flask
import pytest
from sqlalchemy.orm import scoped_session

from core.repositories.authentication import AuthenticationRepository
from app.data.sql.repositories.authentication import AuthenticationSQLRepository
from app.extensions.injection import container


# noinspection PyUnusedLocal
@pytest.fixture(scope="function")
def repo(app: Flask, session: scoped_session) -> AuthenticationSQLRepository:
    return container.get(AuthenticationRepository)
