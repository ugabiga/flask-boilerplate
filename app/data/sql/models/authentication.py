from sqlalchemy import func

from app.core.entities.authentication import Authentication as AuthenticationEntity
from app.extensions.database import sql as db


class Authentication(db.Model):
    __tablename__ = "authentications"

    user_id = db.Column(
        db.BigInteger().with_variant(db.Integer, "sqlite"), primary_key=True
    )
    category = db.Column(db.String(10), primary_key=True)
    identification = db.Column(db.String())
    secret = db.Column(db.String())
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    def to_entity(self) -> AuthenticationEntity:
        return AuthenticationEntity(
            user_id=self.user_id,
            category=self.category,
            identification=self.identification,
            secret=self.secret,
        )
