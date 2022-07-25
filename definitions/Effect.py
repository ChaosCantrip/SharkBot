from datetime import timedelta, datetime


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
            self.expiry = datetime.strptime(expiry, "%S:%M:%H/%d:%m:%Y")

    def extend(self, duration):
        self.expiry = self.expiry + duration

    def convert_to_dict(self):
        data = {
            "id": self.id,
            "expiry": datetime.strftime(self.expiry, "%S:%M:%H/%d:%m:%Y")
        }
        return data


effects = [
    Effect(0, "Money Bag", timedelta(days=1))
]
