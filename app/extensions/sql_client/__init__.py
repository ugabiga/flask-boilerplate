from sqlalchemy.orm import Session

from core.models import BaseModel


class SQLClient:
    def __init__(self, session: Session):
        self.__session = session

    def add(self, model: BaseModel):
        self.__session.add(model)
        self.__session.commit()
