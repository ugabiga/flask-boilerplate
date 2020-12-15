import sqlalchemy as db

from app.extensions.database import sql
from core.entities.users import User as UserEntity
from core.models import BaseModel


class User(sql.Model, BaseModel):
    __tablename__ = "users"

    # noinspection PyTypeChecker
    id = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"), primary_key=True)
    nickname = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def to_entity(self) -> UserEntity:
        # TODO : Add authentications
        return UserEntity(id=self.id, nickname=self.nickname)
