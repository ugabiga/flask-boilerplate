from abc import ABC
from abc import abstractmethod
from typing import Any


class BaseUseCase(ABC):
    @abstractmethod
    def execute(self) -> Any:
        raise NotImplementedError()
