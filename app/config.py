import os

from flask.app import Flask


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hard to guess string"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    REPO_ENGINE = "MYSQL"

    @staticmethod
    def init_app(app: Flask) -> None:
        """
        For testing purpose
        """
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("TEST_DATABASE_URL")
        or f"sqlite:///{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}/test.db"
    )
    WTF_CSRF_ENABLED = False


config = {"default": DevelopmentConfig, "testing": TestingConfig}
