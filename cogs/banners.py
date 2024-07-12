import discord
from discord.ext import commands
import SharkBot


class Banners(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot


async def setup(bot):
    await bot.add_cog(Banners(bot))
    print("Banners Cog Loaded.")


async def teardown(bot):
    await bot.remove_cog("Banners")
    print("Banners Cog Unloaded.")
