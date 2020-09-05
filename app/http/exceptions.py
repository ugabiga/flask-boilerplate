import json
from typing import Tuple

from flask.blueprints import Blueprint
from flask.json import jsonify
from flask.wrappers import Response
from pydantic import ValidationError

from core.use_case_outputs import Failure

error = Blueprint("errors", __name__)


@error.app_errorhandler(ValidationError)
def handle_error(error_: ValidationError) -> Tuple[Response, int]:
    return (
        jsonify(
            {
                "error": Failure.PARAMETERS_ERROR,
                "error_message": "validation_error",
                "error_hint": json.loads(error_.json()),
            }
        ),
        400,
    )
