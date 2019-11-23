from flask import Flask
from sqlalchemy.orm.scoping import scoped_session

from app.core.dtos.tasks import UpdateTaskDto
from app.data.sql.repositories.tasks import TaskSQLRepository


def test_update_task(
        app: Flask, session: scoped_session, repo: TaskSQLRepository
) -> None:
    task_id = 1
    old_task_title = "title"
    old_task_contents = "contents"
    new_task_title = "new title"
    new_task_contents = "new contents"
    dto = UpdateTaskDto(
        task_id=task_id, title=new_task_title, contents=new_task_contents
    )

    repo.create_task(task_id, old_task_title, old_task_contents)
    new_task = repo.update_task(dto)

    if not new_task:
        assert False

    assert new_task.title == new_task_title
    assert new_task.contents == new_task_contents


def test_update_task_empty_dto(
        app: Flask, session: scoped_session, repo: TaskSQLRepository
) -> None:
    task_id = 1
    old_task_title = "title"
    old_task_contents = "contents"
    dto = UpdateTaskDto(task_id=task_id)

    repo.create_task(task_id, old_task_title, old_task_contents)
    new_task = repo.update_task(dto)

    if not new_task:
        assert False

    assert new_task.title == old_task_title
    assert new_task.contents == old_task_contents


def test_update_task_not_found(
        app: Flask, session: scoped_session, repo: TaskSQLRepository
) -> None:
    task_id = 1
    dto = UpdateTaskDto(task_id=task_id)

    new_task = repo.update_task(dto)

    if new_task:
        assert False

    assert True
