from typing import Any, Dict, TypeVar, Type

from pydantic import BaseModel

T = TypeVar("T")


class BaseDto(BaseModel):
    @classmethod
    def validate_from_dict(cls: Type[T], dict_: Dict[str, Any]) -> T:
        return cls(**dict_)  # type: ignore
