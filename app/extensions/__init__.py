from flasgger import Swagger
from flask import Flask

from app.extensions.database import sql
from app.extensions.injection import init_ioc_container
from app.extensions.swagger import get_swagger_config


def init_extensions(app: Flask) -> None:
    sql.init_app(app)
    Swagger(app, **get_swagger_config())
    init_ioc_container()
