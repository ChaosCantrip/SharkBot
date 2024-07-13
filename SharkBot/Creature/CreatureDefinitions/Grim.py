from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class Grim(Creature):

    def __init__(self):
        super().__init__(
            id="grim",
            name="Grim",
            rarity=Rarity.RARE,
            alignment=Alignment.PURPLE,
            base_stats=[500, 200, 200, 0.05, 0.24, 0.04],
            categories=[
                "Destiny",
                "Dread",
                "Video Games"
            ],
            icon_url="https://static0.gamerantimages.com/wordpress/wp-content/uploads/2024/04/destiny-2-the-grim-ezgif-com-webp-to-jpg-converter.jpg"
        )


Grim()
