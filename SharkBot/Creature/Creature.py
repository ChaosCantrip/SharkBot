from typing import Self

from SharkBot.Creature import BaseStats


class Creature:
    creatures: list[Self] = []
    creatures_map: dict[str, Self] = {}

    def __init__(self, id: str, name: str, base_stats: list[int | float]):
        self._id: str = id
        self._name: str = name
        self._base_stats: BaseStats = BaseStats(*base_stats)

        self.creatures.append(self)
        self.creatures_map[id] = self

    # ===== Properties =====

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def base_stats(self) -> BaseStats:
        return self._base_stats
