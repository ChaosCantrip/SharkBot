from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class ShawHan(Creature):

    def __init__(self):
        super().__init__(
            id="shaw_han",
            name="Shaw Han",
            rarity=Rarity.RARE,
            alignment=Alignment.GREEN,
            base_stats=[360, 360, 360, 0.015, 0.015, 0.015],
            categories=[
                "Destiny",
                "Guardian",
                "Hunter",
                "Video Games"
            ],
            icon_url="https://static.wikia.nocookie.net/destinypedia/images/8/8a/Shaw_Han.png/revision/latest?cb=20220330233315"
        )


ShawHan()
