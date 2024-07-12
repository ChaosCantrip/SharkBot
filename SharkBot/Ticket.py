from typing import Self


class Ticket:
    tickets: list[Self] = []
    tickets_map: dict[str, Self] = {}

    def __init__(self, id: str):
        self._id = id

        self.tickets.append(self)
        self.tickets_map[id] = self

    # ===== Properties =====

    @property
    def id(self):
        return self._id

    # ===== Class Methods =====

    @classmethod
    def get(cls, id: str):
        return cls.tickets_map.get(id)


Ticket("hourly_pull")
Ticket("daily_pull")
Ticket("weekly_pull")