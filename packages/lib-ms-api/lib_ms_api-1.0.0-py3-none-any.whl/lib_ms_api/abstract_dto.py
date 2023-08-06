from abc import ABC, abstractmethod
from lib_ms_api import date_util


class AbstractDTO(ABC):

    id: int
    created: int
    modified: int
    modifier_user = str
    valid: bool

    @abstractmethod
    def dto_to_obj(self):
        pass

    @staticmethod
    def serialize_date(date):
        return None if date is None else date_util.get_timestamp(date)
