from flask import Blueprint

api: Blueprint = Blueprint("api", __name__)

from .v1.tasks import *  # noqa isort:skip
from .v1.authentications import *  # noqa isort:skip
