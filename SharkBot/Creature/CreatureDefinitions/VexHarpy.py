from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class VexHarpy(Creature):

    def __init__(self):
        super().__init__(
            id="vex_harpy",
            name="Vex Harpy",
            rarity=Rarity.COMMON,
            alignment=Alignment.BLUE,
            base_stats=[340, 340, 200, 0, 0, 0],
            categories=[
                "Destiny",
                "Vex",
                "Video Games"
            ],
            icon_url="https://destiny.wiki.gallery/images/thumb/3/37/Grimoire_Harpy.jpg/325px-Grimoire_Harpy.jpg"
        )


VexHarpy()
