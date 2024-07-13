from SharkBot.Creature import Creature
from SharkBot import Rarity, Alignment


class KellEcho(Creature):

    def __init__(self):
        super().__init__(
            id="kell_echo",
            name="Kell Echo",
            rarity=Rarity.LEGENDARY,
            alignment=Alignment.GREEN,
            base_stats=[240, 380, 1200, 0.01, 0.12, 0.01],
            categories=[
                "Destiny",
                "Taken",
                "Prophecy",
                "Dungeon Boss",
                "Video Games"
            ],
            icon_url="https://destiny.wiki.gallery/images/e/ec/Kell_Echo.jpg"
        )

    @staticmethod
    def leader_skill_description(level: int):
        rank = self.leader_skill_rank(level)
        amount = [40, 45, 50, 60][level - 1]
        return f"`Dungeon Boss` Units ATK, DEF and HP **+{amount}%**\n`GREEN` Units Evasion Chance **+3%**"

    @staticmethod
    def support_skill_description(level: int):
        return f"TBD"

    @staticmethod
    def unique_ability_description(level: int):
        rank = self.unique_ability_rank(level)
        evasion_amount = [1, 1.2, 1.5, 2][level - 1]
        evasion_max = [10, 15, 18, 20][level - 1]
        additional_defense = [10, 15, 18, 20][level - 1]
        return f"Evasion chance increases by **+{evasion_amount}%** with each attack performed, up to a maximum of **+{evasion_max}%**.\nGain **+{additional_defense}%** DEF for 1 turn after evading an attack."

KellEcho()
