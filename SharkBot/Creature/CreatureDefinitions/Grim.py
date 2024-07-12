from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class Grim(Creature):

    def __init__(self):
        super().__init__(
            id="grim",
            name="Grim",
            rarity=Rarity.RARE,
            alignment=Alignment.PURPLE,
            base_stats=[500, 200, 200, 0.05, 0.24, 0.04],
            categories=[
                "Destiny",
                "Dread",
                "Video Games"
            ]
        )


Grim()
