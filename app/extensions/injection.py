# noinspection PyUnresolvedReferences
from typing import T

from flask import current_app
from flask.config import Config
from werkzeug.local import LocalProxy

from app.core.repositories.tasks import TaskRepository
from app.data.sql.repositories.task import TaskSQLRepository


class IocContainer:
    _injection_dict = {}

    def __init__(self, config: Config) -> None:
        self.config = config
        self._set_repository()

    def get(self, cls: T) -> T:
        return self._injection_dict[cls]()

    def _set_repository(self) -> None:
        self._injection_dict.update({TaskRepository: TaskSQLRepository})


def _get_di_container() -> IocContainer:
    return IocContainer(current_app.config)


# noinspection PyTypeChecker
container: IocContainer = LocalProxy(_get_di_container)
