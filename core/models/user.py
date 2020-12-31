from sqlalchemy.exc import InvalidRequestError

from app.extensions.database import sql as db
from core.entities.users import User as UserEntity
from core.models import BaseModel


class UserModel(db.Model):
    __tablename__ = "users"

    # Columns
    id = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"), primary_key=True)
    nickname = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Relationship
    authentications = db.relationship("AuthenticationModel", lazy="raise")

    def to_entity(self) -> UserEntity:
        user = UserEntity(id=self.id, nickname=self.nickname)
        try:
            user.authentications = [
                authentication for authentication in self.authentications
            ]
        except InvalidRequestError:
            user.authentications = []

        return user
