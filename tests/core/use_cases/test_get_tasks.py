from unittest import mock

from pydantic.error_wrappers import ValidationError

from core.entities.tasks import Task
from core.use_cases.tasks.get_tasks import GetTasksByUserUseCase, GetUserTaskDto


def test_get_user_tasks_dto_validation() -> None:
    raw_input = {
        "user_id": 1,
        "previous_id": "a",
        "limit": 1,
    }
    try:
        GetUserTaskDto.validate_from_dict(raw_input)
    except ValidationError:
        assert True
        return

    assert False


def test_get_all_tasks_with_pagination() -> None:
    mock_tasks = [
        Task(1, 1, "1", "contents"),
        Task(2, 2, "2", "contents"),
        Task(3, 3, "3", "contents"),
        Task(4, 4, "4", "contents"),
    ]

    dto = GetUserTaskDto(user_id=1)
    repo = mock.Mock()
    repo.get_tasks.return_value = mock_tasks

    output = GetTasksByUserUseCase(repo).execute(dto)
    assert True if output.is_success() else False

    assert output.get_data() == mock_tasks
    assert output.get_meta() == {"previous_id": mock_tasks[-1].id, "limit": 10}
