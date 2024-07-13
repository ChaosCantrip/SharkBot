from SharkBot.Creature import BaseStats

STAT_MULTIPLIERS: dict[int, float] = {
    1: 1.0,
    2: 1.05,
    3: 1.1,
    4: 1.2,
    5: 1.3,
    6: 1.4,
    7: 1.5,
    8: 1.6,
    9: 1.7,
    10: 1.8,
    11: 1.85,
    12: 1.9,
    13: 1.95,
    14: 2.0,
    15: 2.05,
    16: 2.1,
    17: 2.15,
    18: 2.2,
    19: 2.25,
    20: 2.35
}


class LevelledStats:

    def __init__(self, base_stats: BaseStats, level: int):
        self._base_stats: BaseStats = base_stats
        self._level: int = level
        self._stat_multiplier: float = STAT_MULTIPLIERS[level]

    # ===== Properties =====

    @property
    def attack(self) -> int:
        return int(self._base_stats.attack * self._stat_multiplier)

    @property
    def defense(self) -> int:
        return int(self._base_stats.defense * self._stat_multiplier)

    @property
    def max_health(self) -> int:
        return int(self._base_stats.max_health * self._stat_multiplier)

    @property
    def critical_chance(self) -> float:
        return self._base_stats.critical_chance * self._stat_multiplier

    @property
    def evade_chance(self) -> float:
        return self._base_stats.evade_chance * self._stat_multiplier

    @property
    def additional_attack_chance(self) -> float:
        return self._base_stats.additional_attack_chance * self._stat_multiplier
