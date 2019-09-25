from flask import Flask

from app.core.repositories.tasks import TaskRepository
from app.data.sql.repositories.tasks import TaskSQLRepository
from app.extensions.injection import container


def test_injecting_repository(app: Flask) -> None:
    repository = container.get(TaskRepository)
    assert type(repository) is TaskSQLRepository
