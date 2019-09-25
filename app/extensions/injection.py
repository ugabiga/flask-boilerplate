from typing import T

from flask import current_app
from werkzeug.local import LocalProxy

from app.core.repositories.tasks import TaskRepository
from app.data.sql.repositories.tasks import TaskSQLRepository


from flask.config import Config
class DependencyInjectionContainer:
    _injection_dict = {}

    def __init__(self, config: Config) -> None:
        self.config = config
        self._set_repository()

    def get(self, cls: T) -> TaskSQLRepository:
        return self._injection_dict[cls]()

    def _set_repository(self) -> None:
        self._injection_dict.update({
            TaskRepository: TaskSQLRepository
        })


def _get_di_container() -> DependencyInjectionContainer:
    return DependencyInjectionContainer(current_app.config)


# noinspection PyTypeChecker
container: DependencyInjectionContainer = LocalProxy(_get_di_container)
