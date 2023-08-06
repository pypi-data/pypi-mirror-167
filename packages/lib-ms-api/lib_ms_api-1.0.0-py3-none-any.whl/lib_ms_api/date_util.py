from datetime import datetime


def get_timestamp(date: datetime):
    return int(round(date.timestamp() * 1000))
