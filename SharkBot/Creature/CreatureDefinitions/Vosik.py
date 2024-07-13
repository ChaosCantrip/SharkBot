from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class Vosik(Creature):

    def __init__(self):
        super().__init__(
            id="vosik",
            name="Vosik",
            rarity=Rarity.LEGENDARY,
            alignment=Alignment.RED,
            base_stats=[950, 360, 600, 0.05, 0.01, 0.1],
            categories=[
                "Destiny",
                "Fallen",
                "SIVA",
                "Raid Boss",
                "Video Games"
            ],
            icon_url="https://static.wikia.nocookie.net/destinypedia/images/9/96/Vosik%2C_the_Archpriest_%28Grimoire_Card%29.jpg/revision/latest?cb=20161020055246"
        )

    def leader_skill_description(self, level: int):
        rank = self.leader_skill_rank(level)
        amount = [25, 30, 35, 40][rank - 1]
        return f"`Fallen` or `RED` Units ATK, DEF and HP **+{amount}%**"

    def support_skill_description(self, level: int):
        return f"`Fallen` Units chance of performing an additional attack **+1.5%**"

    def unique_ability_description(self, level: int):
        rank = self.unique_ability_rank(level)
        amount = [2, 3, 4, 5][rank - 1]
        max_amount = [10, 14, 18, 20][rank - 1]
        return f"ATK increases by **+{amount}%** with each attack performed, up to a maximum of **+{max_amount}%**."


Vosik()
