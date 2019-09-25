import pytest
import os
from app import create_app
from app.extensions.database import sql as _db

from _pytest.fixtures import SubRequest
from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.scoping import scoped_session
TEST_DB = "tests.db"
TEST_DB_PATH = f"{os.path.dirname(os.path.dirname(__file__))}/{TEST_DB}"
TEST_DATABASE_URI = "sqlite:///" + TEST_DB_PATH


# noinspection PyShadowingNames
@pytest.yield_fixture(scope="session")
def app(request: SubRequest) -> Flask:
    settings = {"TESTING": True, "SQLALCHEMY_DATABASE_URI": TEST_DATABASE_URI}
    app = create_app("testing", settings)
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


# noinspection PyShadowingNames
@pytest.fixture(scope="session")
def db(app: Flask, request: SubRequest) -> SQLAlchemy:
    """
    Session-wide tests database.
    http://alexmic.net/flask-sqlalchemy-pytest/
    """

    if os.path.exists(TEST_DB_PATH):
        os.unlink(TEST_DB_PATH)

    def teardown():
        _db.drop_all()
        os.unlink(TEST_DB_PATH)

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope="function")
def session(db: SQLAlchemy, request: SubRequest) -> scoped_session:
    """
    Creates a new data session for a tests.
    http://alexmic.net/flask-sqlalchemy-pytest/
    """
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session
