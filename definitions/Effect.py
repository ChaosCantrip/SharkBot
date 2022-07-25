from datetime import timedelta, datetime

timeFormat = "%S:%M:%H/%d:%m:%Y"


class Effect:

    def __init__(self, effectid: int, name: str, duration: timedelta):
        self.id = effectid
        self.name = name
        self.duration = duration


class AppliedEffect:

    def __init__(self, effectid: int, expiry):
        self.id = effectid
        if expiry is None:
            self.expiry = None
        else:
            self.expiry = datetime.strptime(expiry, timeFormat)

    def extend(self, duration):
        self.expiry = self.expiry + duration

    def convert_to_dict(self):
        data = {
            "id": self.id,
            "expiry": datetime.strftime(self.expiry, timeFormat)
        }
        return data


effects = [
    Effect(0, "Money Bag", timedelta(days=1))
]
