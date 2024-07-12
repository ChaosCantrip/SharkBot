from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class Psion(Creature):

    def __init__(self):
        super().__init__(
            id="psion",
            name="Psion",
            rarity=Rarity.COMMON,
            alignment=Alignment.RED,
            base_stats=[340, 200, 190, 0, 0, 0],
            categories=[
                "Destiny",
                "Cabal",
                "Video Games"
            ]
        )


Psion()
