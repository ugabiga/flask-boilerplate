from app.data.sql.models import BaseModel
from app.extensions.database import sql as db


class User(db.Model, BaseModel):
    __tablename__ = "users"

    id = db.Column(db.BigInteger, primary_key=True)
    nickname = db.Column(db.String(50))
    created_at = db.Column("created_at", db.DateTime)
    updated_at = db.Column("updated_at", db.DateTime)
