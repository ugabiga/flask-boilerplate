from unittest import mock

from app.core.entities.tasks import Task
from app.core.use_cases.get_task import GetTasksUseCase
from app.http.requests.v1.tasks import GetAllTasksRequest


def test_get_all_tasks_with_pagination() -> None:
    mock_tasks = [
        Task(1, 1, "1", "contents"),
        Task(2, 2, "2", "contents"),
        Task(3, 3, "3", "contents"),
        Task(4, 4, "4", "contents"),
    ]

    request = GetAllTasksRequest()
    repo = mock.Mock()
    repo.get_tasks.return_value = mock_tasks

    result = GetTasksUseCase(repo, request).execute()
    if not result:
        assert False

    assert result.get_data() == mock_tasks
    assert result.get_meta() == {"previous_id": mock_tasks[-1].id, "limit": 10}
