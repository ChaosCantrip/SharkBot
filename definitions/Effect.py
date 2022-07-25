from datetime import timedelta


class Effect:

    def __init__(self, effectid: int, name: str, duration: timedelta):
        self.id = effectid
        self.name = name
        self.duration = duration


effects = []
