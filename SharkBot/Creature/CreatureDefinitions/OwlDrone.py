from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class OwlDrone(Creature):

    def __init__(self):
        super().__init__(
            id="owl_drone",
            name="Owl Drone",
            rarity=Rarity.COMMON,
            alignment=Alignment.RED,
            base_stats=[200, 300, 100, 0, 0, 0],
            categories=[
                "Valorant",
                "Video Games"
            ]
        )


OwlDrone()
