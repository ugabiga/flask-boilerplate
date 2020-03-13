import pytest

from app.core.entities.tasks import Task
from app.data.sql.repositories.task import TaskSQLRepository


@pytest.fixture(scope="function", autouse=True)
def clean_up_tasks(repo: TaskSQLRepository) -> None:
    repo.delete_all_tasks()


@pytest.fixture(scope="function")
def old_task(repo: TaskSQLRepository) -> Task:
    user_id = 1
    old_task_title = "title"
    old_task_contents = "contents"
    return repo.create_task(user_id, old_task_title, old_task_contents)


def test_update_task(repo: TaskSQLRepository, old_task: Task) -> None:
    task_id = old_task.id
    new_task_title = "new title"
    new_task_contents = "new contents"
    entity = Task(id=task_id, title=new_task_title, contents=new_task_contents)

    repo.create_task(task_id, old_task.title, old_task.contents)
    new_task = repo.update_task(entity)

    if not new_task:
        assert False

    assert new_task.title == new_task_title
    assert new_task.contents == new_task_contents


def test_update_task_empty_dto(repo: TaskSQLRepository, old_task: Task) -> None:
    entity = Task(id=old_task.id)
    new_task = repo.update_task(entity)

    if not new_task:
        assert False

    assert new_task.title == old_task.title
    assert new_task.contents == old_task.contents


def test_update_task_not_found(repo: TaskSQLRepository) -> None:
    entity = Task(id=1)

    new_task = repo.update_task(entity)

    if new_task:
        assert False

    assert True
