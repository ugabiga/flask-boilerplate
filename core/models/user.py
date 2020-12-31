from app.extensions.database import sql as db
from core.entities.users import User as UserEntity
from core.models.base import BaseModel


class UserModel(BaseModel):
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
        user.authentications = self._attach_related_entities(lambda: [
            authentication.to_entity() for authentication in self.authentications
        ])

        return user
