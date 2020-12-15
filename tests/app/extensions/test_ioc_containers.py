import inject
from flask import Flask

from core.repositories.tasks import TaskRepository


# noinspection PyUnusedLocal
def test_injecting_repository(app: Flask) -> None:
    repository = inject.instance(TaskRepository)
    assert type(repository) is TaskRepository
