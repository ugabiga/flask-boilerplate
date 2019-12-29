from dataclasses import dataclass


@dataclass
class Authentication:
    user_id: int
    category: str
    secret: str
