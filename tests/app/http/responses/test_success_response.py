from flask import Flask

from app.http.responses import build_response
from app.http.responses.tasks import TaskSchema
from core.entities.tasks import Task
from core.use_case_outputs import Success


def test_build_response(app: Flask) -> None:
    task = Task(1, 1, "title", "contents")
    output = Success(task)
    response, status_code = build_response(output, TaskSchema)

    assert status_code == 200
    assert response.json["data"] == vars(task)
