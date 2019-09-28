from typing import Any
from typing import Dict
from typing import Optional

from flask.app import Flask

from app.config import config
from app.extensions.database import sql
from app.http.main import main as main_bp
from app.http.api import api as api_bp


def init_config(app: Flask, config_name: str, settings: Optional[Dict[str, Any]] = None) -> None:
    app_config = config[config_name]
    app.config.from_object(app_config)
    app_config.init_app(app)

    if settings:
        app.config.update(settings)


def init_extensions(app: Flask) -> None:
    if app.config["REPO_ENGINE"] == "MYSQL":
        sql.init_app(app)


def init_blueprints(app: Flask) -> None:
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)


def create_app(config_name: str = "default", settings: Optional[Dict[str, Any]] = None) -> Flask:
    app = Flask(__name__)

    init_config(app, config_name, settings)
    init_extensions(app)
    init_blueprints(app)
    return app
