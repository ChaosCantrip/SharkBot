from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class Phalanx(Creature):

    def __init__(self):
        super().__init__(
            id="phalanx",
            name="Phalanx",
            rarity=Rarity.RARE,
            alignment=Alignment.PURPLE,
            base_stats=[100, 920, 140, 0.025, 0.03, 0.025],
            categories=[
                "Destiny",
                "Cabal",
                "Video Games"
            ]
        )


Phalanx()
