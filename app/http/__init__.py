from flask import Flask

from app.http.api import api
from app.http.main import main


def init_blueprints(app: Flask) -> None:
    app.register_blueprint(main)
    app.register_blueprint(api)
