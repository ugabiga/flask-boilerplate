from typing import Any, Tuple, Type

import marshmallow as ma
from flask import jsonify
from flask.wrappers import Response

from core.use_case_outputs import Failure, Output


def build_success_output_with_schema(
    output: Output, schema_class: Type[ma.Schema], many: bool = None
) -> Tuple[Response, int]:
    output_schema = schema_class().dump(output.get_data(), many=many)

    return build_success_response(output_schema, output.get_meta())


def build_success_response(data: Any, meta: dict = None) -> Tuple[Response, int]:
    response = {"data": data}

    if meta is not None:
        response["meta"] = meta

    return jsonify(response), 200


def build_failure_response(output: Failure) -> Tuple[Response, int]:
    return jsonify(error=output.get_type(), error_message=output.get_message()), 400


def build_response(
    output: Output, schema_class: Type[ma.Schema] = None, many: bool = None
) -> Tuple[Response, int]:
    if output.is_success() and schema_class is not None:
        return build_success_output_with_schema(output, schema_class, many)

    if output.is_success():
        return build_success_response(output.get_data(), output.get_meta())

    if isinstance(output, Failure):
        return build_failure_response(output)

    return build_failure_response(
        Failure.build_empty_internal_response_error("in_response_builder")
    )
