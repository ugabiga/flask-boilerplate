from typing import Any, Type

from flask import jsonify
import marshmallow as ma

from app.http.responses.tasks import TaskSchema
from core.use_case_outputs import Failure, Output


from flask.wrappers import Response


def build_success_output_with_schema(
    output: Output, schema_class: Type[ma.Schema] = None, many: bool = None
) -> Response:
    return build_success_response(
        schema_class().dump(output.get_data(), many=many), output.get_meta()
    )


def build_success_response(data: Any, meta: dict = None) -> Response:
    response = {"data": data}

    if meta is not None:
        response["meta"] = meta

    return jsonify(response)


def build_failure_response(output: Failure):
    return jsonify(error=output.get_type(), error_message=output.get_message()), 400


def build_response(
    output: Output, schema_class: Type[ma.Schema] = None, many: bool = None
) -> Response:
    if output.is_success() and schema_class is not None:
        return build_success_output_with_schema(output, schema_class, many)

    if output.is_success():
        return build_success_response(output.get_data(), output.get_meta())

    if isinstance(output, Failure):
        return build_failure_response(output)
