import os

from app import create_app

app = application = create_app(os.environ.get("FLASK_CONFIG") or "default")
