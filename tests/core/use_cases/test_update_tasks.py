from unittest import mock

from core.entities.tasks import Task
from core.use_cases.update_tasks import UpdateTaskDto, UpdateTaskUseCase


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

    output = UpdateTaskUseCase(repo).execute(dto)
    assert True if output.is_success() else False

    task = output.get_data()
    assert task.id == expected_task.id
    assert task.user_id == expected_task.user_id
    assert task.title == expected_task.title
    assert task.contents == expected_task.contents
