from SharkBot import MemberCreature
from SharkBot.Errors import CreatureNotFoundError


class MemberCreatures:

    def __init__(self, creature_data: list[dict]):
        self._creatures = [MemberCreature(**data) for data in creature_data]
        self._creatures_map = {creature.base_creature.id: creature for creature in self._creatures}

    # ===== Properties =====

    @property
    def creatures(self) -> list[MemberCreature]:
        return list(self._creatures)

    @property
    def data(self) -> list[dict]:
        return [creature.data for creature in self._creatures]

    # ===== Methods =====

    def get(self, base_creature_id: str) -> MemberCreature:
        try:
            return self._creatures_map[base_creature_id]
        except KeyError:
            raise CreatureNotFoundError(base_creature_id)

    def add_power(self, base_creature_id: str, power: int) -> int:
        try:
            creature = self.get(base_creature_id)
        except CreatureNotFoundError:
            creature = MemberCreature(base_creature_id, 0, 0)
            self._creatures.append(creature)
            self._creatures_map[base_creature_id] = creature
        return creature.add_power(power)
