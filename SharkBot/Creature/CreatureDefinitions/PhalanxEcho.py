from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class PhalanxEcho(Creature):

    def __init__(self):
        super().__init__(
            id="phalanx_echo",
            name="Phalanx Echo",
            rarity=Rarity.LEGENDARY,
            alignment=Alignment.RED,
            base_stats=[500, 950, 620, 0.03, 0.03, 0.03],
            categories=[
                "Destiny",
                "Taken",
                "Prophecy",
                "Dungeon Boss",
                "Video Games"
            ],
            icon_url="https://destiny.wiki.gallery/images/1/18/PhalanxEcho.jpg"
        )

    def leader_skill_description(self, level: int):
        rank = self.leader_skill_rank(level)
        amount_1 = [40, 45, 50, 60][rank - 1]
        amount_2 = [20, 25, 30, 35][rank - 1]
        return f"`Prophecy` Units ATK, DEF and HP **+{amount_1}%**\n`RED` Units ATK, DEF and HP **+{amount_2}%**"

    def support_skill_description(self, level: int):
        return f"TBD"

    def unique_ability_description(self, level: int):
        rank = self.unique_ability_rank(level)
        amount = [2, 3, 4, 5][rank - 1]
        max_amount = [10, 14, 18, 20][rank - 1]
        return f"DEF increases by **+{amount}%** with each attack received, up to a maximum of **+{max_amount}%**."


PhalanxEcho()
