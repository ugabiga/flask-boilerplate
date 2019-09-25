from flask import Blueprint

from .v1.tasks import *  # noqa

api = Blueprint("api", __name__)
