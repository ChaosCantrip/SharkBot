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
