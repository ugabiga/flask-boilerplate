from abc import ABC, abstractmethod

from voluptuous import MultipleInvalid, Schema


class BaseRequest(ABC):
    @classmethod
    @abstractmethod
    def _get_validation_schema(cls) -> Schema:
        raise NotImplementedError()

    @classmethod
    def from_dict(cls, dict_):
        try:
            cls._get_validation_schema()(dict_)
        except MultipleInvalid as exception:
            raise exception

        # noinspection PyArgumentList
        return cls(**dict_)
