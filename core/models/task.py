import sqlalchemy as db

from core.entities.tasks import Task as TaskEntity
from core.models.base import BaseModel


class TaskModel(BaseModel):
    __tablename__ = "tasks"
    __table_args__ = {"sqlite_autoincrement": True}

    # noinspection PyTypeChecker
    id = db.Column(
        db.BigInteger().with_variant(db.Integer, "sqlite"),
        primary_key=True,
        autoincrement=True,
    )
    user_id = db.Column(db.BigInteger)
    title = db.Column(db.String(100))
    contents = db.Column(db.TEXT)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def to_entity(self) -> TaskEntity:
        return TaskEntity(
            id=self.id, user_id=self.user_id, title=self.title, contents=self.contents
        )
