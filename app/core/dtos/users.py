from dataclasses import dataclass
from typing import Optional


@dataclass
class CreateUserDto:
    nickname: str
