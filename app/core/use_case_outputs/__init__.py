from abc import ABC
from typing import Any
from typing import Optional


class UseCaseSuccessOutput(ABC):
    def __bool__(self):
        raise NotImplementedError()

    def get_type(self) -> Any:
        raise NotImplementedError()

    def get_data(self) -> Any:
        raise NotImplementedError()

    def get_meta(self) -> Any:
        raise NotImplementedError()


class BaseUseCaseSuccessOutput(UseCaseSuccessOutput):
    SUCCESS = "success"

    def __bool__(self) -> bool:
        return True

    def get_type(self) -> str:
        return self.SUCCESS

    def get_data(self) -> Any:
        raise NotImplementedError()

    def get_meta(self) -> Any:
        raise NotImplementedError()


class UseCaseFailureOutput:
    RESOURCE_ERROR = "resource_error"
    PARAMETERS_ERROR = "parameters_error"
    SYSTEM_ERROR = "system_error"
    NOT_FOUND_ERROR = "not_found_error"

    def __init__(self, type_: str, code: int, message: str) -> None:
        self.type = type_
        self.code = code
        self.message = self._format_message(message)

    def __bool__(self) -> bool:
        return False

    @classmethod
    def build_not_found_error(cls, message: Optional[str] = None) -> Any:
        return cls(cls.NOT_FOUND_ERROR, 404, message)

    def _format_message(self, msg: str) -> str:
        if isinstance(msg, Exception):
            return "{}: {}".format(msg.__class__.__name__, "{}".format(msg))
        return msg
