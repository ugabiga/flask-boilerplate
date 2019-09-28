from unittest import mock

from app.core.entities.tasks import Task
from app.core.use_cases.tasks import CreateTaskUseCase
from app.http.requests.v1.tasks import CreateTaskRequest


def test_create_task():
    expected_task = Task(1, 1, "title", "contents")

    request = CreateTaskRequest(
        user_id=expected_task.user_id,
        title=expected_task.title,
        contents=expected_task.contents,
    )
    repo = mock.Mock()
    repo.create_task.return_value = expected_task

    result = CreateTaskUseCase(repo, request).execute()
    assert result

    task = result.get_data()
    assert type(task) is Task
    assert task.user_id is expected_task.user_id
    assert task.title is expected_task.title
    assert task.contents is expected_task.contents


def test_fail_to_create_task():
    request_task = Task(1, 1, "title", "contents")

    request = CreateTaskRequest(
        user_id=request_task.user_id,
        title=request_task.title,
        contents=request_task.contents,
    )
    repo = mock.Mock()
    repo.create_task.return_value = None

    result = CreateTaskUseCase(repo, request).execute()

    if result:
        assert False

    assert True
