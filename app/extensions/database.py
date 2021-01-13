from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session

sql = SQLAlchemy()
session: Session = sql.session
