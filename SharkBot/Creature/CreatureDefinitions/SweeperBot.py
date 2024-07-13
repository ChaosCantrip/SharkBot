from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class SweeperBot(Creature):

    def __init__(self):
        super().__init__(
            id="sweeper_bot",
            name="Sweeper Bot",
            rarity=Rarity.COMMON,
            alignment=Alignment.GREEN,
            base_stats=[15, 800, 200, 0, 0, 0],
            categories=[
                "Destiny",
                "Video Games"
            ],
            icon_url="https://cdn.mos.cms.futurecdn.net/pujnqysTeTjpQYfqCQNNhb.jpg"
        )


SweeperBot()
