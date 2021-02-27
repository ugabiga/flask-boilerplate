from flask import Flask

from app.http.api import api
from app.http.api.root import root
from app.http.exceptions import error


def init_blueprints(app: Flask) -> None:
    app.register_blueprint(root)
    app.register_blueprint(api)
    app.register_blueprint(error)
