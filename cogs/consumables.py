import discord
from discord.ext import tasks, commands

import secret

if secret.testBot:
    import testids as ids
else:
    import ids


class Consumables(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Consumables(bot))
    print("Consumables Cog loaded")


def teardown(bot):
    print("Consumables Cog unloaded")
    bot.remove_cog(Consumables(bot))
