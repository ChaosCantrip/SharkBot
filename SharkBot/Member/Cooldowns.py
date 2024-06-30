from datetime import timedelta, datetime

_TIME_FORMAT = "%d/%m/%Y-%H:%M:%S"


class Cooldown:

    def __init__(self, duration: timedelta, expiry: str):
        self.duration: timedelta = duration
        self.expiry: datetime = datetime.strptime(expiry, _TIME_FORMAT)

    @property
    def expired(self) -> bool:
        return datetime.utcnow() > self.expiry


class Cooldowns:
    pass
