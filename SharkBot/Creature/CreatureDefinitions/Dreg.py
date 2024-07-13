from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class Dreg(Creature):

    def __init__(self):
        super().__init__(
            id="dreg",
            name="Dreg",
            rarity=Rarity.COMMON,
            alignment=Alignment.BLUE,
            base_stats=[400, 80, 95, 0, 0, 0],
            categories=[
                "Destiny",
                "Fallen",
                "Video Games"
            ],
            icon_url="https://static.wikia.nocookie.net/destinypedia/images/c/cc/Dreg.png/revision/latest?cb=20130510122121"
        )


Dreg()
