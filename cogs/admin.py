import discord
from discord.ext import commands
import SharkBot


class Admin(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot


async def setup(bot):
    await bot.add_cog(Admin(bot))
    print("Admin Cog Loaded.")


async def teardown(bot):
    await bot.remove_cog("Admin")
    print("Admin Cog Unloaded.")
