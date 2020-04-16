from unittest import mock

from core.entities.tasks import Task
from core.use_case_outputs import UseCaseFailureOutput
from core.use_cases.update_tasks import (
    UpdateTaskDto,
    UpdateTaskUseCase,
    UpdateTaskUseCaseOutput,
)


def test_update_task() -> None:
    task_id = 1
    user_id = 1
    title = "title"
    contents = "contents"
    expected_task = Task(task_id, user_id, title, contents)
    dto = UpdateTaskDto(task_id, user_id, title, contents)

    repo = mock.Mock()
    repo.read_task.return_value = expected_task
    repo.update_task.return_value = expected_task

    result = UpdateTaskUseCase(repo).execute(dto)

    assert type(result) is not UseCaseFailureOutput
    assert type(result) is UpdateTaskUseCaseOutput

    assert result.get_data().id == expected_task.id
    assert result.get_data().user_id == expected_task.user_id
    assert result.get_data().title == expected_task.title
    assert result.get_data().contents == expected_task.contents
