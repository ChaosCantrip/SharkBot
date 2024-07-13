from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class Vosik(Creature):

    def __init__(self):
        super().__init__(
            id="vosik",
            name="Vosik",
            rarity=Rarity.LEGENDARY,
            alignment=Alignment.RED,
            base_stats=[950, 360, 600, 0.05, 0.01, 0.1],
            categories=[
                "Destiny",
                "Fallen",
                "SIVA",
                "Raid Boss",
                "Video Games"
            ],
            icon_url="https://static.wikia.nocookie.net/destinypedia/images/9/96/Vosik%2C_the_Archpriest_%28Grimoire_Card%29.jpg/revision/latest?cb=20161020055246"
        )


Vosik()
