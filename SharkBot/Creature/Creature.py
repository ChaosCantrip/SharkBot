from typing import Self, Optional
import difflib
from SharkBot.Creature import BaseStats
from SharkBot.Errors import CreatureNotFoundError
from SharkBot.Rarity import Rarity
from SharkBot.Alignment import Alignment


class Creature:
    creatures: list[Self] = []
    creatures_map: dict[str, Self] = {}

    def __init__(self, id: str, name: str, base_stats: list[int | float], categories: list[str], rarity: Rarity,
                 alignment: Alignment, icon_url: str):
        self._id: str = id
        self._name: str = name
        self._base_stats: BaseStats = BaseStats(*base_stats)
        self._categories: list[str] = categories
        self._rarity: Rarity = rarity
        self._alignment: Alignment = alignment
        self._icon_url: str = icon_url

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
    def rarity(self) -> Rarity:
        return self._rarity

    @property
    def alignment(self) -> Alignment:
        return self._alignment

    @property
    def base_stats(self) -> BaseStats:
        return self._base_stats

    @property
    def categories(self) -> list[str]:
        return list(self._categories)

    @property
    def icon_url(self) -> str:
        return self._icon_url

    # ===== Class Methods =====

    @classmethod
    def get(cls, id: str) -> Self:
        try:
            return cls.creatures_map[id]
        except KeyError:
            raise CreatureNotFoundError(id)

    @classmethod
    def search(cls, name: str, accuracy: float = 0.7) -> Self:
        name = name.lower()
        creature_ids = cls.creatures_map.keys()
        closest_match = difflib.get_close_matches(name, creature_ids, n=1, cutoff=accuracy)
        if closest_match:
            return cls.creatures_map[closest_match[0]]
        else:
            raise CreatureNotFoundError(name)

    # ===== Skill Ranks =====

    @staticmethod
    def leader_skill_rank(level: int) -> int:
        if level >= 18:
            return 4
        elif level >= 10:
            return 3
        elif level >= 5:
            return 2
        else:
            return 1

    @staticmethod
    def unique_ability_rank(level: int) -> int:
        if level >= 20:
            return 4
        elif level >= 12:
            return 3
        elif level >= 7:
            return 2
        else:
            return 1

    # ===== Abilities =====

    @staticmethod
    def leader_skill_description(level: int) -> Optional[str]:
        """
        Will be set within Creature subclasses.
        :param level:
        :return:
        """
        return None

    @staticmethod
    def support_skill_description(level: int) -> Optional[str]:
        """
        Will be set within Creature subclasses.
        :param level:
        :return:
        """
        return None

    @staticmethod
    def unique_ability_description(level: int) -> Optional[str]:
        """
        Will be set within Creature subclasses.
        :param level:
        :return:
        """
        return None
