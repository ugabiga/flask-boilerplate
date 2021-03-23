from dataclasses import dataclass, field
from typing import List

from core.entities.authentication import Authentication
from core.entities.base import BaseDataclass


@dataclass
class User(BaseDataclass):
    id: int
    nickname: str

    authentications: List[Authentication] = field(default_factory=lambda: [])
