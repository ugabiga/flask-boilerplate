from unittest import mock

from core.entities.tasks import Task
from core.use_cases.tasks.create_tasks import CreateTaskDto, CreateTaskUseCase


def test_create_task() -> None:
    expected_task = Task(1, 1, "title", "contents")

    dto = CreateTaskDto(
        user_id=expected_task.user_id,
        title=expected_task.title,
        contents=expected_task.contents,
    )

    repo = mock.Mock()
    repo.create_task.return_value = expected_task

    output = CreateTaskUseCase(repo).execute(dto)
    assert True if output.is_success() else False

    task = output.get_data()
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

    output = CreateTaskUseCase(repo).execute(dto)

    assert False if output.is_success() else True
