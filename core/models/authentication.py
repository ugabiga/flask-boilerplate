from app.extensions.database import sql as db
from core.entities.authentication import Authentication as AuthenticationEntity


class AuthenticationModel(db.Model):
    __tablename__ = "authentications"

    # noinspection PyTypeChecker
    user_id = db.Column(
        db.BigInteger().with_variant(db.Integer, "sqlite"),
        db.ForeignKey("users.id"),
        primary_key=True,
    )
    category = db.Column(db.String(10), primary_key=True)
    identification = db.Column(db.String())
    secret = db.Column(db.String())
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def to_entity(self) -> AuthenticationEntity:
        return AuthenticationEntity(
            user_id=self.user_id,
            category=self.category,
            identification=self.identification,
            secret=self.secret,
        )
