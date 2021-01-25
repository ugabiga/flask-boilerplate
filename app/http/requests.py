import functools
from typing import Callable, Type

from flask import abort, jsonify, make_response, request
from pydantic import ValidationError

from core.use_cases.authentications.create_token import CreateTokenDto


def validate_request(dto_cls: Type[CreateTokenDto]) -> Callable:
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                kwargs["dto"] = dto_cls.validate_from_dict(request.get_json())
            except ValidationError as e:
                abort(make_response(jsonify(error=e.errors()), 400))
            return func(*args, **kwargs)

        return wrapper

    return decorator
