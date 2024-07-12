from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class VexGoblin(Creature):

    def __init__(self):
        super().__init__(
            id="vex_goblin",
            name="Vex Goblin",
            rarity=Rarity.COMMON,
            alignment=Alignment.GREEN,
            base_stats=[140, 400, 140, 0, 0, 0],
            categories=[
                "Destiny",
                "Vex",
                "Video Games"
            ]
        )


VexGoblin()
