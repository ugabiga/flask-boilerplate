from core.entities.tasks import Task
from core.repositories.tasks import TaskRepository


def test_create_task(repo: TaskRepository) -> None:
    task = repo.create_task(1, "hello", "this is contents")
    assert type(task) is Task
