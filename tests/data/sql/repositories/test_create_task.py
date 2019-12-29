from flask import Flask
from sqlalchemy.orm.scoping import scoped_session

from app.core.entities.tasks import Task
from app.data.sql.repositories.tasks import TaskSQLRepository


def test_create_task(
    app: Flask, session: scoped_session, repo: TaskSQLRepository
) -> None:
    task = repo.create_task(1, "hello", "this is contents")
    assert type(task) is Task
