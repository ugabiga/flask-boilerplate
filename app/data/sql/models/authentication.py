from app.data.sql.models import BaseModel
from app.core.entities.authentication import Authentication as AuthenticationEntity
from app.extensions.database import sql as db


class Authentication(db.Model, BaseModel):
    __tablename__ = "authentications"

    user_id = db.Column(db.BigInteger)
    category = db.Column(db.String(10))
    secret = db.Column(db.String())
    created_at = db.Column("created_at", db.DateTime)
    updated_at = db.Column("updated_at", db.DateTime)

    def to_entity(self) -> AuthenticationEntity:
        return AuthenticationEntity(
            user_id=self.user_id, category=self.category, secret=self.secret
        )
