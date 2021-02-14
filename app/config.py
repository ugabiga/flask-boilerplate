import os

from flask.app import Flask


class Config:
    # Default
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hard to guess string"

    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("SQLALCHEMY_DATABASE_URI") or "sqlite:///:memory:"
    )

    # CSRF
    WTF_CSRF_ENABLED = True

    # Message
    MESSAGE_BASE_URL = os.environ.get("MESSAGE_BASE_URL", "app-kafka:9093")
    MESSAGE_CONSUMER_GROUP_ID = os.environ.get(
        "MESSAGE_CONSUMER_GROUP_ID", "message_group_1"
    )


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("TEST_DATABASE_URL")
        or f"sqlite:///{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}/test.db"
    )
    WTF_CSRF_ENABLED = False


def init_config(app: Flask, config_name: str) -> None:
    config = {
        "default": DevelopmentConfig,
        "development": DevelopmentConfig,
        "testing": TestingConfig,
    }
    app_config = config[config_name]
    app.config.from_object(app_config)
