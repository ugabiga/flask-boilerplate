from flask.app import Flask

from app.config import init_config
from app.extensions import init_extensions
from app.http import init_blueprints


def create_app(config_name: str = "default") -> Flask:
    app = Flask(__name__)

    init_config(app, config_name)
    init_extensions(app)
    init_blueprints(app)

    return app
