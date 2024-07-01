import discord
from discord.ext import commands
import SharkBot


class Admin(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @SharkBot.Checks.Permissions.is_admin()
    async def op(self, ctx: commands.Context, member: discord.Member):
        sharkbot_member = SharkBot.Member.get(member.id)
        sharkbot_member.permissions.admin = True
        sharkbot_member.write_data()
        await ctx.send(f"{member.mention} is now an admin.")

    @commands.command()
    @SharkBot.Checks.Permissions.is_admin()
    async def deop(self, ctx: commands.Context, member: discord.Member):
        sharkbot_member = SharkBot.Member.get(member.id)
        sharkbot_member.permissions.admin = False
        sharkbot_member.write_data()
        await ctx.send(f"{member.mention} is no longer an admin.")

async def setup(bot):
    await bot.add_cog(Admin(bot))
    print("Admin Cog Loaded.")


async def teardown(bot):
    await bot.remove_cog("Admin")
    print("Admin Cog Unloaded.")
