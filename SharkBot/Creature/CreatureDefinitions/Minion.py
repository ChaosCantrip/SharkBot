from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class Minion(Creature):

    def __init__(self):
        super().__init__(
            id="minion",
            name="Minion",
            rarity=Rarity.COMMON,
            alignment=Alignment.BLUE,
            base_stats=[240, 340, 140, 0, 0, 0],
            categories=[
                "League of Legends",
                "Video Games"
            ],
            icon_url="https://static.wikia.nocookie.net/leagueoflegends/images/7/78/Order_Minion_Caster_Render.png/revision/latest?cb=20200601043520"
        )


Minion()
