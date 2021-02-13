import os

from app import create_app

app = application = create_app(os.environ.get("ENV") or "default")
