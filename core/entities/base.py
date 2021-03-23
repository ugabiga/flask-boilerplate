from dataclasses import asdict, dataclass


@dataclass
class BaseDataclass:
    def to_dict(self):
        return asdict(self)
