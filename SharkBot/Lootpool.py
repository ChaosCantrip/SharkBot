from typing import Self
from SharkBot import Errors

class Lootpool:
    lootpools: list[Self] = []
    lootpools_map: dict[str, Self] = {}


    def __init__(self, id: str, rewards: list[dict]):
        self.id: str = id
        self._rewards: list[dict] = rewards

    @classmethod
    def get(cls, lootpool_id: str):
        try:
            return cls.lootpools_map[lootpool_id]
        except ValueError:
            raise Errors.LootpoolNotFoundError(lootpool_id)
            