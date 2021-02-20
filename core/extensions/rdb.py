from __future__ import annotations

import inspect
from typing import Generic, List, TypeVar

T = TypeVar("T")


class Query(Generic[T]):
    def __init__(self, model: T) -> None:
        self.__session = self.__init_session()

        if not inspect.isclass(model):
            self.__model = model
        else:
            self.__model_cls = model
            self.__q = self.__session.query(self.__model_cls)

    def __init_session(self):
        from app.extensions.database import session

        return session

    def create(self) -> T:
        self.__session.add(self.__model)
        self.__session.commit()
        self.__session.refresh(self.__model)
        self._close()
        return self.__model

    def filter(self, *criterion) -> Query:
        self.__q = self.__q.filter(*criterion)
        return self

    def order_by(self, *criterion) -> Query:
        self.__q = self.__q.order_by(*criterion)
        return self

    def limit(self, limit: int) -> Query:
        self.__q = self.__q.limit(limit)
        return self

    def all(self) -> List[T]:
        result = self.__q.all()
        self._close()
        return result

    def one_or_none(self) -> T:
        result = self.__q.first()
        self._close()
        return result

    def update(self, *dict_value) -> int:
        result = self.__q.update(*dict_value)
        self.__session.commit()
        self._close()
        return result

    def delete(self) -> bool:
        self.__q.delete()
        self.__session.commit()
        self._close()
        return True

    def _close(self) -> None:
        self.__q = None
