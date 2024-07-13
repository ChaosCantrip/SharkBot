from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class Vorgeth(Creature):

    def __init__(self):
        super().__init__(
            id="vorgeth",
            name="Vorgeth",
            rarity=Rarity.LEGENDARY,
            alignment=Alignment.YELLOW,
            base_stats=[400, 800, 600, 0.045, 0, 0.015],
            categories=[
                "Destiny",
                "Taken",
                "Shattered Throne",
                "Dungeon Boss",
                "Video Games"
            ],
            icon_url="https://destiny.wiki.gallery/images/c/c8/Vorgeth_front.jpg"
        )


Vorgeth()
