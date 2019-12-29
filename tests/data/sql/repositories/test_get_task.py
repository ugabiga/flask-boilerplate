from flask import Flask
from sqlalchemy.orm import scoped_session

from app.core.entities.tasks import Task
from app.data.sql.repositories.tasks import TaskSQLRepository


def test_read_tasks_without_previous_id(
    app: Flask, session: scoped_session, repo: TaskSQLRepository
) -> None:
    # Create Sample Data
    [repo.create_task(i, f"{i}", f"{i}") for i in range(0, 10)]

    tasks = repo.get_tasks(0, 5)

    # Assert limit count
    assert len(tasks) == 5

    # Assert type
    for task in tasks:
        assert type(task) is Task
