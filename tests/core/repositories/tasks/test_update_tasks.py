import pytest

from core.entities.tasks import Task
from core.repositories.tasks import TaskRepository


@pytest.fixture(scope="function", autouse=True)
def clean_up_tasks(repo: TaskRepository) -> None:
    repo.delete_all_tasks()


@pytest.fixture(scope="function")
def old_task(repo: TaskRepository) -> Task:
    user_id = 1
    old_task_title = "title"
    old_task_contents = "contents"
    return repo.create_task(user_id, old_task_title, old_task_contents)


def test_update_task(repo: TaskRepository, old_task: Task) -> None:
    task_id = old_task.id
    user_id = 1
    new_task_title = "new title"
    new_task_contents = "new contents"
    entity = Task(
        id=task_id, user_id=user_id, title=new_task_title, contents=new_task_contents
    )

    repo.create_task(task_id, old_task.title, old_task.contents)
    new_task = repo.update_task(entity.id, entity.title, entity.contents)

    if not new_task:
        assert False

    assert new_task.title == new_task_title
    assert new_task.contents == new_task_contents


def test_update_task_empty_dto(repo: TaskRepository, old_task: Task) -> None:
    entity = Task(id=old_task.id, user_id=1, title="new title", contents="new contents")
    new_task = repo.update_task(entity.id)

    if not new_task:
        assert False

    assert new_task.title == old_task.title
    assert new_task.contents == old_task.contents


def test_update_task_not_found(repo: TaskRepository) -> None:
    entity = Task(id=1, user_id=1, title="title", contents="contents")

    new_task = repo.update_task(entity.id)

    if new_task:
        assert False

    assert True
