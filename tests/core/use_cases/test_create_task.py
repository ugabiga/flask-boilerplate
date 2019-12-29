from unittest import mock

from app.core.dtos.tasks import CreateTaskDto
from app.core.entities.tasks import Task
from app.core.use_cases.create_task import CreateTaskUseCase


def test_create_task() -> None:
    expected_task = Task(1, 1, "title", "contents")

    dto = CreateTaskDto(
        user_id=expected_task.user_id,
        title=expected_task.title,
        contents=expected_task.contents,
    )

    repo = mock.Mock()
    repo.create_task.return_value = expected_task

    result = CreateTaskUseCase(repo, dto).execute()
    assert result

    task = result.get_data()
    assert type(task) is Task
    assert task.user_id is expected_task.user_id
    assert task.title is expected_task.title
    assert task.contents is expected_task.contents


def test_create_task_repository_fail() -> None:
    request_task = Task(1, 1, "title", "contents")

    dto = CreateTaskDto(
        user_id=request_task.user_id,
        title=request_task.title,
        contents=request_task.contents,
    )
    repo = mock.Mock()
    repo.create_task.return_value = None

    result = CreateTaskUseCase(repo, dto).execute()

    if result:
        assert False

    assert True
