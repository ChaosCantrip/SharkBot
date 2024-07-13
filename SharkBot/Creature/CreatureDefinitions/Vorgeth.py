from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class Vorgeth(Creature):

    def __init__(self):
        super().__init__(
            id="vorgeth",
            name="Vorgeth",
            rarity=Rarity.LEGENDARY,
            alignment=Alignment.YELLOW,
            base_stats=[400, 800, 600, 0.045, 0, 0.015],
            categories=[
                "Destiny",
                "Taken",
                "Shattered Throne",
                "Dungeon Boss",
                "Video Games"
            ],
            icon_url="https://destiny.wiki.gallery/images/c/c8/Vorgeth_front.jpg"
        )

    def leader_skill_description(self, level: int):
        rank = self.leader_skill_rank(level)
        amount_1 = [40, 45, 50, 60][rank - 1]
        amount_2 = [20, 25, 30, 35][rank - 1]
        return f"`Shattered Throne` Units ATK, DEF and HP **+{amount_1}%**\n`YELLOW` Units ATK, DEF and HP **+{amount_2}%**"

    def support_skill_description(self, level: int):
        return f"`Taken` Units chance of performing a critical hit **+2%**"

    def unique_ability_description(self, level: int):
        rank = self.unique_ability_rank(level)
        dr_amount = [60, 65, 70, 75][rank - 1]
        def_amount = [1, 1.5, 2, 2.5][rank - 1]
        def_max = [3, 4.5, 6, 7.5][rank - 1]
        return f"Reduces damage received from the first attack by **{dr_amount}%**.\nGain **+{def_amount}%** DEF with each attack received, up to a maximum of **+{def_max}%**."


Vorgeth()
