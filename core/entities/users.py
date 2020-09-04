from dataclasses import dataclass, field
from typing import List

from core.entities.authentication import Authentication


@dataclass
class User:
    id: int
    nickname: str

    authentications: List[Authentication] = field(default_factory=lambda: [])
