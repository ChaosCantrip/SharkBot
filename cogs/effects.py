import discord
from discord.ext import tasks, commands

import secret

if secret.testBot:
    import testids as ids
else:
    import ids


class Effects(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Effects(bot))
    print("Effects Cog loaded")


def teardown(bot):
    print("Effects Cog unloaded")
    bot.remove_cog(Effects(bot))
