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

    uc = CreateTaskUseCase(repo)
    result = uc.execute(request)

    assert type(result) is Task
    assert result.user_id is expected_task.user_id
    assert result.title is expected_task.title
    assert result.contents is expected_task.contents
