class Rarity:

    def __init__(self, name: str, emoji: str):
        self._name: str = name
        self._emoji: str = emoji

    # ===== Properties =====

    @property
    def name(self) -> str:
        return self._name

    @property
    def emoji(self) -> str:
        return self._emoji


COMMON = Rarity("Common", "<:common:1261483012864872529>")
RARE = Rarity("Rare", "<:rare:1261483011766222998>")
LEGENDARY = Rarity("Legendary", "<:legendary:1261483010214334567>")
MYTHIC = Rarity("Mythic", "<:mythic:1261483009312292905>")
