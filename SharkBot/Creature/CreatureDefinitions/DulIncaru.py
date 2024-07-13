from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class DulIncaru(Creature):

    def __init__(self):
        super().__init__(
            id="dul_incaru",
            name="Dul Incaru",
            rarity=Rarity.LEGENDARY,
            alignment=Alignment.BLUE,
            base_stats=[1200, 200, 200, 0.04, 0.07, 0.005],
            categories=[
                "Destiny",
                "Taken",
                "Shattered Throne",
                "Dungeon Boss",
                "Video Games"
            ],
            icon_url="https://destiny.wiki.gallery/images/7/74/Dul_Incaru_the_Eternal_Return.jpg"
        )

    def leader_skill_description(self, level: int):
        rank = self.leader_skill_rank(level)
        amount = [40, 45, 50, 60][rank - 1]
        return f"`Dungeon Boss` Units ATK, DEF and HP **+{amount}%**\n`BLUE` Units Evasion Chance **+3%**"

    def support_skill_description(self, level: int):
        return f"TBD"

    def unique_ability_description(self, level: int):
        rank = self.unique_ability_rank(level)
        evasion_amount = [1, 1.2, 1.5, 2][rank - 1]
        evasion_max = [10, 11.5, 13, 15][rank - 1]
        additional_defense = [10, 15, 18, 20][rank - 1]
        return f"Evasion chance increases by **+{evasion_amount}%** with each attack performed, up to a maximum of **+{evasion_max}%**.\nGain **+{additional_defense}%** ATK for 1 turn after evading an attack."


DulIncaru()
