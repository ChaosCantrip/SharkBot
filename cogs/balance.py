import discord
from discord.ext import commands

import SharkBot


class Balance(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["bal", "b"])
    async def balance(self, ctx: commands.Context):
        member = SharkBot.Member.get(ctx.author.id)
        embed = discord.Embed()
        embed.title = f"{ctx.author.display_name}'s Balance"
        embed.description = f"Your balance is {member.balance}."
        embed.set_thumbnail(url=ctx.author.display_avatar.url)
        embed.colour = discord.Colour.gold()

        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Balance(bot))
    print("Balance Cog Loaded.")


async def teardown(bot):
    await bot.remove_cog("Balance")
    print("Balance Cog Unloaded.")
