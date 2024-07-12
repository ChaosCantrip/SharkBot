from . import Creature, LevelledStats

LEVEL_THRESHOLDS: list[int] = [
    100,
    200,
    300,
    400,
    500,
    700,
    900,
    1200,
    1500,
    2000,
    2500,
    3000,
    4000,
    5000,
    6000,
    7000,
    8000,
    9000,
    10000,
    15000
]


class MemberCreature:

    def __init__(self, base_creature_id: str, power: int, last_handled_level: int):
        self._base_creature: Creature = Creature.get(base_creature_id)
        self._power: int = power
        self.last_handled_level: int = last_handled_level

    # ===== Properties =====

    @property
    def id(self):
        return self._base_creature.id

    @property
    def name(self):
        return self._base_creature.name

    @property
    def rarity(self):
        return self._base_creature.rarity

    @property
    def alignment(self):
        return self._base_creature.alignment

    @property
    def icon_url(self) -> str:
        return self._base_creature.icon_url

    @property
    def base_creature(self) -> Creature:
        return self._base_creature

    @property
    def power(self) -> int:
        return self._power

    @property
    def level(self) -> int:
        for i, threshold in enumerate(LEVEL_THRESHOLDS):
            if self.power < threshold:
                return i
        return len(LEVEL_THRESHOLDS)

    @property
    def stats(self) -> LevelledStats:
        return LevelledStats(self._base_creature.base_stats, self.level)

    @property
    def data(self) -> dict:
        return {
            "base_creature_id": self._base_creature.id,
            "power": self.power,
            "last_handled_level": self.last_handled_level
        }

    # ===== Power Methods =====

    def add_power(self, power: int) -> int:
        over_power = 0
        self._power += power
        if self._power > LEVEL_THRESHOLDS[-1]:
            over_power = self._power - LEVEL_THRESHOLDS[-1]
            self._power = LEVEL_THRESHOLDS[-1]
        return over_power

    # ===== Abilities =====

    @property
    def leader_skill_description(self):
        return self._base_creature.leader_skill_description(self.level)

    @property
    def support_skill_description(self):
        return self._base_creature.support_skill_description(self.level)

    @property
    def unique_ability_description(self):
        return self._base_creature.unique_ability_description(self.level)
