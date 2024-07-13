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
            ],
            icon_url="https://www.bungie.net/common/destiny_content/grimoire/hr_images/203120_7ba749a80ba56b4f3daf7dea92aac9a9.jpg"
        )


VexGoblin()
