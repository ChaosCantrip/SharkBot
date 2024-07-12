from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class TakenHobgoblin(Creature):

    def __init__(self):
        super().__init__(
            id="taken_hobgoblin",
            name="Taken Hobgoblin",
            rarity=Rarity.RARE,
            alignment=Alignment.RED,
            base_stats=[1000, 100, 100, 0.03, 0, 0.125],
            categories=[
                "Destiny",
                "Taken",
                "Video Games"
            ],
            icon_url="https://destiny.wiki.gallery/images/6/68/Grimoire_Taken_Hobgoblin.jpg"
        )


TakenHobgoblin()
