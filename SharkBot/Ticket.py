from typing import Self


class Ticket:
    tickets: list[Self] = []
    tickets_map: dict[str, Self] = {}

    def __init__(self, id: str, name: str):
        self._id = id
        self._name = name

        self.tickets.append(self)
        self.tickets_map[id] = self

    # ===== Properties =====

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    # ===== Class Methods =====

    @classmethod
    def get(cls, id: str):
        return cls.tickets_map.get(id)


Ticket("hourly_pull", "Hourly Pull Ticket")
Ticket("daily_pull", "Daily Pull Ticket")
Ticket("weekly_pull", "Weekly Pull Ticket")