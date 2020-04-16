from flask import Flask
import inject

from app.data.sql.repositories.task import TaskSQLRepository
from core.repositories.tasks import TaskRepository


# noinspection PyUnusedLocal
def test_injecting_repository(app: Flask) -> None:
    repository = inject.instance(TaskRepository)
    assert type(repository) is TaskSQLRepository
