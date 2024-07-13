from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class Phalanx(Creature):

    def __init__(self):
        super().__init__(
            id="phalanx",
            name="Phalanx",
            rarity=Rarity.RARE,
            alignment=Alignment.PURPLE,
            base_stats=[100, 920, 140, 0.025, 0.03, 0.025],
            categories=[
                "Destiny",
                "Cabal",
                "Video Games"
            ],
            icon_url="https://destiny.wiki.gallery/images/thumb/2/2e/Phalanx_%28RL%29.jpg/1200px-Phalanx_%28RL%29.jpg"
        )


Phalanx()
