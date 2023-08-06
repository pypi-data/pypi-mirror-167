from flask_sqlalchemy import Model, SQLAlchemy
from abc import ABC, abstractmethod
from datetime import datetime


class AbstractRepository(ABC):

    @abstractmethod
    def get_model(self) -> Model:
        pass

    @abstractmethod
    def get_database(self) -> SQLAlchemy:
        pass

    def find(self):
        return self.get_model().query.all()

    def get(self, id: int):
        record = self.get_model().query.get(id)
        if record is None:
            return None
        else:
            return record

    def save(self, record):
        if record.id is None:
            self.get_database().session.add(record)
        else:
            record.modified = datetime.now()

        self.get_database().session.commit()
        return record

    def delete(self, id: int):
        record = self.get(id)
        if record is None:
            return False
        else:
            self.get_database().session.delete(record)
            self.get_database().session.commit()
            return True
