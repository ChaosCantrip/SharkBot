from datetime import timedelta, datetime
from definitions import SharkErrors

timeFormat = "%S:%M:%H/%d:%m:%Y"


class Effect:

    def __init__(self, effectid: int, name: str):
        self.id = effectid
        self.name = name


class AppliedEffect:

    def __init__(self, effectdata):
        self.id = effectdata["id"]
        if effectdata["expiry"] is None:
            self.expiry = None
        else:
            self.expiry = datetime.strptime(effectdata["expiry"], timeFormat)

    def extend(self, duration):
        self.expiry = self.expiry + duration

    def convert_to_dict(self):
        data = {
            "id": self.id,
            "expiry": datetime.strftime(self.expiry, timeFormat)
        }
        return data


effects = [
    Effect(0, "Money Bag")
]
