from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session

from app.extensions.sql_client import SQLClient

sql = SQLAlchemy()
session: Session = sql.session
sql_client = SQLClient(session)
