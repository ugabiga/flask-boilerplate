from dataclasses import dataclass

from core.entities.base import BaseDataclass


@dataclass
class Authentication(BaseDataclass):
    EMAIL = "email"

    user_id: int
    category: str
    identification: str
    secret: str
