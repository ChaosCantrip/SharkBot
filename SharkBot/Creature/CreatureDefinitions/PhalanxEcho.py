from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class PhalanxEcho(Creature):

    def __init__(self):
        super().__init__(
            id="phalanx_echo",
            name="Phalanx Echo",
            rarity=Rarity.LEGENDARY,
            alignment=Alignment.RED,
            base_stats=[500, 950, 620, 0.03, 0.03, 0.03],
            categories=[
                "Destiny",
                "Taken",
                "Prophecy",
                "Dungeon Boss",
                "Video Games"
            ],
            icon_url="https://destiny.wiki.gallery/images/1/18/PhalanxEcho.jpg"
        )


PhalanxEcho()
