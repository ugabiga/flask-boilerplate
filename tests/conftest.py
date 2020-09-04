import pytest
from _pytest.fixtures import SubRequest  # type: ignore
from flask.app import Flask
from sqlalchemy.orm.scoping import scoped_session  # type: ignore

from app import create_app
from app.extensions.database import sql as _db
from tests.helper.request import RequestClient


# noinspection PyShadowingNames
@pytest.yield_fixture(scope="session")
def app(request: SubRequest) -> Flask:
    app = create_app("testing")
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


# noinspection PyShadowingNames
@pytest.fixture(scope="function")
def client(app: Flask) -> RequestClient:
    return RequestClient(app.test_client())


# noinspection PyShadowingNames
@pytest.yield_fixture(scope="function")
def session(app: Flask, request: SubRequest) -> scoped_session:
    def teardown():
        _db.session.rollback()
        _db.drop_all()
        _db.session.commit()

    _db.app = app
    _db.drop_all()
    _db.create_all()

    request.addfinalizer(teardown)

    return _db.session
