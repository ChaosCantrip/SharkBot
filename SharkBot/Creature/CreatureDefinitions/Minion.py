from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class Minion(Creature):

    def __init__(self):
        super().__init__(
            id="minion",
            name="Minion",
            rarity=Rarity.COMMON,
            alignment=Alignment.BLUE,
            base_stats=[240, 340, 140, 0, 0, 0],
            categories=[
                "League of Legends",
                "Video Games"
            ]
        )


Minion()
