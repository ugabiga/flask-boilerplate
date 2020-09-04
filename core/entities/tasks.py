from dataclasses import dataclass


@dataclass
class Task:
    id: int
    user_id: int
    title: str
    contents: str
