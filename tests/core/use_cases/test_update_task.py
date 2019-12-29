from unittest import mock

from app.core.entities.tasks import Task
from app.core.use_case_outputs import UseCaseFailureOutput
from app.core.use_case_outputs.tasks import UpdateTaskUseCaseSuccessOutput
from app.core.use_cases.update_task import UpdateTaskUseCase
from app.http.requests.v1.tasks import UpdateTaskRequest


def test_update_task() -> None:
    task_id = 1
    user_id = 1
    title = "title"
    contents = "contents"
    expected_task = Task(task_id, user_id, title, contents)

    req = UpdateTaskRequest(
        expected_task.id, expected_task.title, expected_task.contents
    )

    repo = mock.Mock()
    repo.read_task.return_value = expected_task
    repo.update_task.return_value = expected_task

    result = UpdateTaskUseCase(repo, user_id, req).execute()

    assert type(result) is not UseCaseFailureOutput
    assert type(result) is UpdateTaskUseCaseSuccessOutput

    assert result.get_data().id == expected_task.id
    assert result.get_data().user_id == expected_task.user_id
    assert result.get_data().title == expected_task.title
    assert result.get_data().contents == expected_task.contents
