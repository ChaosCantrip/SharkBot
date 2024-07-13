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
            ],
            icon_url="https://ams3.digitaloceanspaces.com/web01.ho-sting/videogamesartwork_com/public/concept-art/1603635331/valorant--character--sova-drone-01--by-larry-ray.jpg"
        )


OwlDrone()
