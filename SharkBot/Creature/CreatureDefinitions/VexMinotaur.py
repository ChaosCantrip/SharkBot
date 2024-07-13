from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class VexMinotaur(Creature):

    def __init__(self):
        super().__init__(
            id="vex_minotaur",
            name="Vex Minotaur",
            rarity=Rarity.RARE,
            alignment=Alignment.YELLOW,
            base_stats=[300, 300, 500, 0.01, 0.06, 0.025],
            categories=[
                "Destiny",
                "Vex",
                "Video Games"
            ],
            icon_url="https://www.bungie.net/common/destiny_content/grimoire/hr_images/203140_1f1a5d3bb8f7ec7e73f19023df0f0ba6.jpg"
        )


VexMinotaur()
