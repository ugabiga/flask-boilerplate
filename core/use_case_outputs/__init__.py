from __future__ import annotations

from typing import Generic, TypeVar

_ValueType = TypeVar("_ValueType", covariant=True)


class Output(Generic[_ValueType]):
    _data: _ValueType

    def get_data(self) -> _ValueType:
        raise NotImplementedError

    def get_meta(self) -> dict:
        raise NotImplementedError

    def is_success(self) -> bool:
        raise NotImplementedError


class Failure(Output[_ValueType]):
    RESOURCE_ERROR = "resource_error"
    PARAMETERS_ERROR = "parameters_error"
    SYSTEM_ERROR = "system_error"
    NOT_FOUND_ERROR = "not_found_error"
    NOT_AUTHORIZED_ERROR = "not_authorized_error"
    EMPTY_INTERNAL_RESPONSE_ERROR = "empty_internal_response_error"

    def __init__(self, error_type: str, error_message: str = "") -> None:
        self._error_type = error_type
        self._error_message = error_message

    def is_success(self) -> bool:
        return False

    def get_meta(self) -> dict:
        return {}

    def get_data(self) -> _ValueType:
        raise NotImplementedError

    def get_type(self) -> str:
        return self._error_type

    def get_message(self) -> str:
        return self._error_message

    @classmethod
    def build_not_found_error(cls, error_message: str = "") -> Failure:
        return cls(cls.NOT_FOUND_ERROR, error_message)

    @classmethod
    def build_parameter_error(cls, error_message: str = "") -> Failure:
        return cls(cls.PARAMETERS_ERROR, error_message)

    @classmethod
    def build_not_authorized_error(cls, error_message: str = "") -> Failure:
        return cls(cls.NOT_AUTHORIZED_ERROR, error_message)

    @classmethod
    def build_empty_internal_response_error(cls, error_message: str = ""):
        return cls(cls.EMPTY_INTERNAL_RESPONSE_ERROR, error_message)


class Success(Output[_ValueType]):
    def __init__(self, data: _ValueType, meta: dict = None) -> None:
        self._data = data
        self._meta = {} if meta is None else meta

    def is_success(self) -> bool:
        return True

    def get_meta(self) -> dict:
        return self._meta

    def get_data(self) -> _ValueType:
        return self._data
