class BaseStats:

    def __init__(self, attack: int, defense: int, max_health: int, critical_chance: float, evade_chance: float,
                 additional_attack_chance: float):
        self._attack = attack
        self._defense = defense
        self._max_health = max_health
        self._critical_chance = critical_chance
        self._evade_chance = evade_chance
        self._additional_attack_chance = additional_attack_chance

    @property
    def attack(self) -> int:
        return self._attack

    @property
    def defense(self) -> int:
        return self._defense

    @property
    def max_health(self) -> int:
        return self._max_health

    @property
    def critical_chance(self) -> float:
        return self._critical_chance

    @property
    def evade_chance(self) -> float:
        return self._evade_chance

    @property
    def additional_attack_chance(self) -> float:
        return self._additional_attack_chance
