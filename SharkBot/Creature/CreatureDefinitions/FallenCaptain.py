from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class FallenCaptain(Creature):

    def __init__(self):
        super().__init__(
            id="fallen_captain",
            name="Fallen Captain",
            rarity=Rarity.RARE,
            alignment=Alignment.GREEN,
            base_stats=[200, 400, 400, 0.01, 0.01, 0.1],
            categories=[
                "Destiny",
                "Fallen",
                "Video Games"
            ]
        )


FallenCaptain()
