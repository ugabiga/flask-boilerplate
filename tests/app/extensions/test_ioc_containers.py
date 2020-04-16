from flask import Flask

from app.data.sql.repositories.task import TaskSQLRepository
from app.extensions.injection import container
from core.repositories.tasks import TaskRepository


# noinspection PyUnusedLocal
def test_injecting_repository(app: Flask) -> None:
    repository = container.get(TaskRepository)
    assert type(repository) is TaskSQLRepository
