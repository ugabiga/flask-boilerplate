from flask import Flask
import inject
from inject import Binder

from app.data.sql.repositories.authentication import AuthenticationSQLRepository
from app.data.sql.repositories.task import TaskSQLRepository
from core.repositories.authentication import AuthenticationRepository
from core.repositories.tasks import TaskRepository


def bind(binder: Binder, app: Flask):
    binder.bind_to_provider(TaskRepository, TaskSQLRepository)
    binder.bind_to_provider(AuthenticationRepository, AuthenticationSQLRepository)


def init_ioc_container(app: Flask) -> None:
    inject.clear_and_configure(lambda binder: bind(binder, app))
