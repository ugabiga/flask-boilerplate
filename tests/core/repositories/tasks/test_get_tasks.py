from core.entities.tasks import Task
from core.repositories.tasks import TaskRepository


def test_read_tasks_without_previous_id(repo: TaskRepository) -> None:
    # Create Sample Data
    [repo.create_task(i, f"{i}", f"{i}") for i in range(0, 10)]

    tasks = repo.get_tasks(0, 5)

    # Assert limit count
    assert len(tasks) == 5

    # Assert type
    for task in tasks:
        assert type(task) is Task
