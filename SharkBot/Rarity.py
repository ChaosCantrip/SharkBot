class _Rarity:

    def __init__(self, name: str):
        self._name: str = name

    # ===== Properties =====

    @property
    def name(self) -> str:
        return self._name


COMMON = _Rarity("Common")
RARE = _Rarity("Rare")
LEGENDARY = _Rarity("Legendary")
MYTHIC = _Rarity("Mythic")
