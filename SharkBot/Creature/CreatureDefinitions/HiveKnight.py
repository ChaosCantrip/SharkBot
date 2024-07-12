from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class HiveKnight(Creature):

    def __init__(self):
        super().__init__(
            id="hive_knight",
            name="Hive Knight",
            rarity=Rarity.RARE,
            alignment=Alignment.BLUE,
            base_stats=[620, 400, 250, 0.085, 0.0035, 0.025],
            categories=[
                "Destiny",
                "Hive",
                "Video Games"
            ],
            icon_url="https://destiny.wiki.gallery/images/2/2f/Grimoire_Knight.jpg"
        )


HiveKnight()
