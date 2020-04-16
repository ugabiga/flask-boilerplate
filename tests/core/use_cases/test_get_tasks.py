from unittest import mock

from core.entities.tasks import Task
from core.use_cases.get_tasks import GetUserTasksDto, GetUserTasksUseCase


def test_get_all_tasks_with_pagination() -> None:
    mock_tasks = [
        Task(1, 1, "1", "contents"),
        Task(2, 2, "2", "contents"),
        Task(3, 3, "3", "contents"),
        Task(4, 4, "4", "contents"),
    ]

    dto = GetUserTasksDto(1)
    repo = mock.Mock()
    repo.get_tasks.return_value = mock_tasks

    result = GetUserTasksUseCase(repo).execute(dto)
    if not result:
        assert False

    assert result.get_data() == mock_tasks
    assert result.get_meta() == {"previous_id": mock_tasks[-1].id, "limit": 10}
