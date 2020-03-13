from typing import Any

from flask import jsonify

from app.core.use_case_outputs import UseCaseFailureOutput


import marshmallow as ma
from app.http.responses.tasks import TaskSchema
from flask.wrappers import Response
from typing import Type


def build_failure_response(use_case_output: UseCaseFailureOutput):
    return (
        jsonify(error=use_case_output.type, error_description=use_case_output.message),
        use_case_output.code,
    )


def build_success_response(*args, meta=None, **kwargs) -> Response:
    if args and kwargs:
        raise TypeError("Can not use both args and kwargs at the same time")
    elif len(args) == 1:
        data = args[0]
    else:
        data = args or kwargs

    output = {"data": data}
    if meta is not None:
        output["meta"] = meta

    return jsonify(output)


def build_success_dump_response(
    schema_class: Type[ma.Schema], data: Any, many: bool = None
) -> Response:
    return build_success_response(schema_class().dump(data, many=many))
