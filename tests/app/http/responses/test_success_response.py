from flask import Flask

from core.entities.tasks import Task
from app.http.responses import build_success_dump_response
from app.http.responses.tasks import TaskSchema


# noinspection PyUnusedLocal
def test_build_success_dump_response(app: Flask) -> None:
    expected_task = Task(1, 1, "title", "contents")
    response = build_success_dump_response(TaskSchema, expected_task)
    assert response
