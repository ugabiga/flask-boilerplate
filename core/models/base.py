from typing import Callable

from sqlalchemy.exc import InvalidRequestError

from app.extensions.database import sql as db


class BaseModel(db.Model):
    __abstract__ = True

    def _attach_related_entities(self, list_function: Callable):
        try:
            return list_function()
        except InvalidRequestError:
            return []
