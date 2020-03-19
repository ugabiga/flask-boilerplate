from dataclasses import dataclass
from dataclasses import field
from typing import List

from app.core.entities.authentication import Authentication


@dataclass
class User:
    id: int = None
    nickname: str = None

    authentications: List[Authentication] = field(default_factory=lambda: [])
