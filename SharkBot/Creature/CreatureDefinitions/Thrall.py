from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class Thrall(Creature):

    def __init__(self):
        super().__init__(
            id="thrall",
            name="Thrall",
            rarity=Rarity.COMMON,
            alignment=Alignment.YELLOW,
            base_stats=[400, 80, 95, 0, 0, 0],
            categories=[
                "Destiny",
                "Hive",
                "Video Games"
            ]
        )


Thrall()
