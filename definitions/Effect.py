from datetime import timedelta, datetime


class Effect:

    def __init__(self, effectid: int, name: str, duration: timedelta):
        self.id = effectid
        self.name = name
        self.duration = duration


class AppliedEffect:

    def __init__(self, effectid: int):
        self.id = effectid


effects = [
    Effect(0, "Money Bag", timedelta(days=1))
]
