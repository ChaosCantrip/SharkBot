from datetime import timedelta, datetime
from definitions import SharkErrors

timeFormat = "%S:%M:%H/%d:%m:%Y"


class Effect:

    def __init__(self, effectid: int, name: str):
        self.id = effectid
        self.name = name


class AppliedEffect:

    def __init__(self, effectdata):
        self.effect = get(effectdata["id"])
        if effectdata["expiry"] is None:
            self.expiry = None
        else:
            self.expiry = datetime.strptime(effectdata["expiry"], timeFormat)

    def extend(self, duration):
        self.expiry = self.expiry + duration

    def set_expiry(self, expiry):
        self.expiry = expiry

    def check_expired(self):
        dtnow = datetime.now()
        if self.expiry is None:
            return False
        elif self.expiry > dtnow:
            return False
        else:
            return True

    def get_expiry_text(self):
        if self.expiry is None:
            return "No Expiry"
        else:
            return datetime.strftime(self.expiry, timeFormat)

    def convert_to_dict(self):
        data = {
            "id": self.effect.id
        }
        if self.expiry is None:
            data["expiry"] = None
        else:
            data["expiry"] = datetime.strftime(self.expiry, timeFormat)
        return data


class NewEffect(AppliedEffect):

    def __init__(self, effectid, duration):
        self.effect = get(effectid)
        if duration is None:
            self.expiry = None
        else:
            self.expiry = datetime.now() + duration


effects = [
    Effect(0, "Money Bags"),
    Effect(1, "Counting Charm")
]


def get(search):
    for effect in effects:
        if effect.name == search:
            return effect
    search = int(search)
    for effect in effects:
        if effect.id == search:
            return effect
    raise SharkErrors.EffectNotFoundError(search)
