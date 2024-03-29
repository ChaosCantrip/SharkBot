from datetime import datetime, timedelta
from typing import Optional

from SharkBot import Utils

_TIME_FORMAT = "%d/%m/%Y-%H:%M:%S"


class Cooldown:

    def __init__(self, name: str, duration: timedelta, expiry: Optional[str] = None) -> None:
        self.name = name
        if expiry is None:
            self.expiry = datetime.utcnow() - duration
        else:
            self.expiry = datetime.strptime(expiry, _TIME_FORMAT)
        self.duration = duration

    @property
    def expired(self) -> bool:
        return datetime.utcnow() > self.expiry

    def extend(self) -> None:
        self.expiry += self.duration

    def reset(self) -> None:
        self.expiry = datetime.utcnow() + self.duration

    @property
    def timestring(self) -> str:
        return datetime.strftime(self.expiry, _TIME_FORMAT)

    @property
    def time_remaining(self) -> timedelta:
        return self.expiry - datetime.utcnow()

    @property
    def time_remaining_string(self) -> str:
        return Utils.td_to_string(self.time_remaining)

    @property
    def data(self) -> str:
        return datetime.strftime(self.expiry, _TIME_FORMAT)

    @property
    def db_data(self) -> dict[str, str | int]:
        return {
            "name": self.name.capitalize(),
            "expiry": int(self.expiry.timestamp() * 1000)
        }
