import jwt
from abc import ABC, abstractmethod
from lib_ms_api.abstract_repository import AbstractRepository


def generate_jwt_token(payload, secret: str, algorithm: str):
    return jwt.encode(payload, secret, algorithm)


def decode_jwt_token(token: str, secret: str, algorithm: str):
    return jwt.decode(token, secret, algorithm)


# noinspection PyMethodMayBeStatic
class AbstractService(ABC):

    @abstractmethod
    def _get_repository(self) -> AbstractRepository:
        pass

    @abstractmethod
    def _map_to_update(self, new_record, record_db):
        pass

    def _contains(self, record):
        return False

    def get_list(self):
        return self._get_repository().find()

    def get_by_id(self, id: int):
        return self._get_repository().get(id)

    def create(self, record):
        if self._contains(record):
            return None
        else:
            record.id = None
            return self._get_repository().save(record)

    def update(self, id: int, new_record):
        record_db = self.get_by_id(id)

        if record_db is None:
            return None

        self._map_to_update(new_record, record_db)
        record_db.modifier_user = new_record.modifier_user

        return self._get_repository().save(record_db)

    def delete(self, id: int):
        return self._get_repository().delete(id)
