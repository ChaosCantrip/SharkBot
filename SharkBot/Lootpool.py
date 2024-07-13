import random
from typing import Self


class CurrencyReward:

    def __init__(self, currency: str, min: int, max: int):
        self._currency: str = currency
        self._min: int = min
        self._max: int = max
        self._amount: int = random.randint(self._min, self._max)

    @property
    def currency(self):
        return self._currency

    @property
    def amount(self):
        return self._amount


class PowerReward:

    def __init__(self, creature_id: str, amount: int):
        self._creature_id: str = creature_id
        self._amount: int = amount

    @property
    def creature_id(self):
        return self._creature_id

    @property
    def amount(self):
        return self._amount


class TicketReward:

    def __init__(self, ticket_id: str, amount: int):
        self._ticket_id: str = ticket_id
        self._amount: int = amount

    @property
    def ticket_id(self):
        return self._ticket_id

    @property
    def amount(self):
        return self._amount


class LootpoolReward:

    def __init__(self, lootpool_id: str):
        self._lootpool_id: str = lootpool_id

    @property
    def lootpool_id(self):
        return self._lootpool_id


class LootpoolNode:

    def __init__(self, chance: float, reward: CurrencyReward | PowerReward | TicketReward | LootpoolReward):
        self._chance: float = chance
        self._reward: CurrencyReward | PowerReward | TicketReward | LootpoolReward = reward

    @property
    def chance(self):
        return self._chance

    @property
    def reward(self):
        return self._reward


class Lootpool:
    lootpools: list[Self] = []
    lootpools_map: dict[str, Self] = {}

    def __init__(self, id: str, pool: list[LootpoolNode]):
        self._id: str = id
        self._pool: list[LootpoolNode] = pool

        self.lootpools.append(self)
        self.lootpools_map[id] = self

    @property
    def id(self):
        return self._id

    @property
    def pool(self):
        return self._pool

    @classmethod
    def get(cls, lootpool_id: str):
        return cls.lootpools_map[lootpool_id]

    def roll(self) -> CurrencyReward | PowerReward | TicketReward:
        reward = random.choices([node.reward for node in self.pool], [node.chance for node in self.pool])[0]
        if type(reward) is LootpoolReward:
            lootpool = Lootpool.get(reward.lootpool_id)
            return lootpool.roll()
        return reward

# THIS IS TEMPORARY
# AND HORRIBLE
# I'm sorry

from SharkBot import Creature, Rarity

common_creature_ids = [creature.id for creature in Creature.creatures if creature.rarity is Rarity.COMMON]
rare_creature_ids = [creature.id for creature in Creature.creatures if creature.rarity is Rarity.RARE]
legendary_creature_ids = [creature.id for creature in Creature.creatures if creature.rarity is Rarity.LEGENDARY]

Lootpool(
    id="hourly_pull_common",
    pool=[
        LootpoolNode(chance=1, reward=PowerReward(creature_id, 20))
        for creature_id in common_creature_ids
    ]
)
Lootpool(
    id="hourly_pull_rare",
    pool=[
        LootpoolNode(chance=1, reward=PowerReward(creature_id, 20))
        for creature_id in rare_creature_ids
    ]
)
Lootpool(
    id="hourly_pull_legendary",
    pool=[
        LootpoolNode(chance=1, reward=PowerReward(creature_id, 20))
        for creature_id in legendary_creature_ids
    ]
)
Lootpool(
    id="daily_pull_common",
    pool=[
        LootpoolNode(chance=1, reward=PowerReward(creature_id, 50))
        for creature_id in common_creature_ids
    ]
)
Lootpool(
    id="daily_pull_rare",
    pool=[
        LootpoolNode(chance=1, reward=PowerReward(creature_id, 50))
        for creature_id in rare_creature_ids
    ]
)
Lootpool(
    id="daily_pull_legendary",
    pool=[
        LootpoolNode(chance=1, reward=PowerReward(creature_id, 50))
        for creature_id in legendary_creature_ids
    ]
)
Lootpool(
    id="weekly_pull_common",
    pool=[
        LootpoolNode(chance=1, reward=PowerReward(creature_id, 100))
        for creature_id in common_creature_ids
    ]
)
Lootpool(
    id="weekly_pull_rare",
    pool=[
        LootpoolNode(chance=1, reward=PowerReward(creature_id, 100))
        for creature_id in rare_creature_ids
    ]
)
Lootpool(
    id="weekly_pull_legendary",
    pool=[
        LootpoolNode(chance=1, reward=PowerReward(creature_id, 100))
        for creature_id in legendary_creature_ids
    ]
)
Lootpool(
    id="hourly_pull",
    pool=[
        LootpoolNode(chance=0.45, reward=LootpoolReward("hourly_pull_common")),
        LootpoolNode(chance=0.4, reward=LootpoolReward("hourly_pull_rare")),
        LootpoolNode(chance=0.15, reward=LootpoolReward("hourly_pull_legendary"))
    ]
)
Lootpool(
    id="daily_pull",
    pool=[
        LootpoolNode(chance=0.45, reward=LootpoolReward("daily_pull_common")),
        LootpoolNode(chance=0.4, reward=LootpoolReward("daily_pull_rare")),
        LootpoolNode(chance=0.15, reward=LootpoolReward("daily_pull_legendary"))
    ]
)
Lootpool(
    id="weekly_pull",
    pool=[
        LootpoolNode(chance=0.45, reward=LootpoolReward("weekly_pull_common")),
        LootpoolNode(chance=0.4, reward=LootpoolReward("weekly_pull_rare")),
        LootpoolNode(chance=0.15, reward=LootpoolReward("weekly_pull_legendary"))
    ]
)