from unittest import mock

from app.core.entities.tasks import Task
from app.core.use_cases.tasks import CreateTaskUseCase
from app.core.use_cases.tasks import GetAllTasksUseCase
from app.http.requests.v1.tasks import CreateTaskRequest
from app.http.requests.v1.tasks import GetAllTasksRequest


def test_create_task() -> None:
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


def test_create_task_repository_fail() -> None:
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


def test_get_all_tasks_with_pagination() -> None:
    mock_tasks = [
        Task(1, 1, "1", "contents"),
        Task(2, 2, "2", "contents"),
        Task(3, 3, "3", "contents"),
        Task(4, 4, "4", "contents"),
    ]

    request = GetAllTasksRequest()
    repo = mock.Mock()
    repo.read_tasks.return_value = mock_tasks

    result = GetAllTasksUseCase(repo, request).execute()
    if not result:
        assert False

    assert result.get_data() == mock_tasks
    assert result.get_meta() == {"previous_id": mock_tasks[-1].id, "limit": 10}
