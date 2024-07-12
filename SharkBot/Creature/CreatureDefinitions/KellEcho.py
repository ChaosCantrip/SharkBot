from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class KellEcho(Creature):

    def __init__(self):
        super().__init__(
            id="kell_echo",
            name="Kell Echo",
            rarity=Rarity.LEGENDARY,
            alignment=Alignment.GREEN,
            base_stats=[240, 380, 1200, 0.01, 0.12, 0.01],
            categories=[
                "Destiny",
                "Taken",
                "Prophecy",
                "Dungeon Boss",
                "Video Games"
            ]
        )


KellEcho()
