import inject
from inject import Binder

from core.repositories.authentication import AuthenticationRepository
from core.repositories.tasks import TaskRepository


def bind(binder: Binder) -> None:
    binder.bind_to_provider(TaskRepository, TaskRepository)
    binder.bind_to_provider(AuthenticationRepository, AuthenticationRepository)


def init_ioc_container() -> None:
    inject.clear_and_configure(lambda binder: bind(binder))
