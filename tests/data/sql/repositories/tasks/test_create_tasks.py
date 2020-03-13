from app.core.entities.tasks import Task
from app.data.sql.repositories.task import TaskSQLRepository


def test_create_task(repo: TaskSQLRepository) -> None:
    task = repo.create_task(1, "hello", "this is contents")
    assert type(task) is Task
