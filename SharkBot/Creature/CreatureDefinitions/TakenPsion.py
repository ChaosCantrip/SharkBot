from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class TakenPsion(Creature):

    def __init__(self):
        super().__init__(
            id="taken_psion",
            name="Taken Psion",
            rarity=Rarity.COMMON,
            alignment=Alignment.PURPLE,
            base_stats=[620, 10, 60, 0, 0, 0],
            categories=[
                "Destiny",
                "Taken",
                "Video Games"
            ],
            icon_url="https://destiny.wiki.gallery/images/3/3e/Grimoire_Taken_Psion.jpg"
        )


TakenPsion()
