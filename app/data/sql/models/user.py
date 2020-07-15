from sqlalchemy import func

from app.data.sql.models import BaseModel
from app.extensions.database import sql as db
from core.entities.users import User as UserEntity


class User(db.Model, BaseModel):
    __tablename__ = "users"

    id = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"), primary_key=True)
    nickname = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    def to_entity(self) -> UserEntity:
        # TODO : Add authentications
        return UserEntity(id=self.id, nickname=self.nickname)
