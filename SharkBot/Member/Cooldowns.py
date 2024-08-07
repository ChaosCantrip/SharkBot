from datetime import timedelta, datetime

import humanize

_TIME_FORMAT = "%d/%m/%Y-%H:%M:%S"


class Cooldown:

    def __init__(self, duration: timedelta, expiry: str):
        self.duration: timedelta = duration
        self.expiry: datetime = datetime.strptime(expiry, _TIME_FORMAT)

    @property
    def expired(self) -> bool:
        return datetime.utcnow() > self.expiry

    def reset(self):
        self.expiry = datetime.utcnow() + self.duration

    def unexpire(self):
        self.expiry = datetime.fromtimestamp(0)

    @property
    def time_remaining(self) -> timedelta:
        return self.expiry - datetime.utcnow()

    @property
    def time_remaining_string(self) -> str:
        return humanize.precisedelta(self.time_remaining, format="%0.0f")

    @property
    def data(self) -> str:
        return datetime.strftime(self.expiry, _TIME_FORMAT)



class Cooldowns:

    def __init__(self, hourly: str, daily: str, weekly: str):
        self.hourly: Cooldown = Cooldown(timedelta(hours=1), hourly)
        self.daily: Cooldown = Cooldown(timedelta(days=1), daily)
        self.weekly: Cooldown = Cooldown(timedelta(weeks=1), weekly)

    @property
    def data(self) -> dict:
        return {
            "hourly": self.hourly.data,
            "daily": self.daily.data,
            "weekly": self.weekly.data
        }