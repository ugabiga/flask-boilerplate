from dataclasses import dataclass


@dataclass
class Task:
    id: int = None
    user_id: int = None
    title: str = None
    contents: str = None
