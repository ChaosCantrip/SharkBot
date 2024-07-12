class Rarity:

    def __init__(self, name: str):
        self._name: str = name

    # ===== Properties =====

    @property
    def name(self) -> str:
        return self._name


COMMON = Rarity("Common")
RARE = Rarity("Rare")
LEGENDARY = Rarity("Legendary")
MYTHIC = Rarity("Mythic")
