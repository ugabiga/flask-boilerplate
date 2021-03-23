from dataclasses import dataclass


@dataclass
class BaseDataclass:
    _hidden_fields = []

    def asdict(self):
        return {k: v for k, v in self.__dict__.items() if k not in self._hidden_fields}
