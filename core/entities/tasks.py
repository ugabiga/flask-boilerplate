from dataclasses import dataclass

from core.entities.base import BaseDataclass


@dataclass
class Task(BaseDataclass):
    id: int
    user_id: int
    title: str
    contents: str
