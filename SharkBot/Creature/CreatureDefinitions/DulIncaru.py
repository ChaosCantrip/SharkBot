from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class DulIncaru(Creature):

    def __init__(self):
        super().__init__(
            id="dul_incaru",
            name="Dul Incaru",
            rarity=Rarity.LEGENDARY,
            alignment=Alignment.BLUE,
            base_stats=[1200, 200, 200, 0.04, 0.07, 0.005],
            categories=[
                "Destiny",
                "Taken",
                "Shattered Throne",
                "Dungeon Boss",
                "Video Games"
            ],
            icon_url="https://destiny.wiki.gallery/images/7/74/Dul_Incaru_the_Eternal_Return.jpg"
        )


DulIncaru()
