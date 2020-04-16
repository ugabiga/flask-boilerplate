from dataclasses import dataclass


@dataclass
class Authentication:
    EMAIL = "email"

    user_id: int
    category: str
    identification: str
    secret: str
