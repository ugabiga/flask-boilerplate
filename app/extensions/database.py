from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session  # type: ignore

sql = SQLAlchemy()
sql_session: Session = sql.session
