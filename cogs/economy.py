import discord
from discord.ext import commands

import SharkBot


class Economy(commands.Cog):

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

    @commands.command()
    @commands.is_owner()
    async def add_balance(self, ctx: commands.Context, member: discord.Member, amount: int):
        sharkbot_member = SharkBot.Member.get(member.id)
        sharkbot_member.balance += amount
        await ctx.reply(f"Added ${amount} to {member.display_name}'s balance.")

    @commands.command()
    @commands.is_owner()
    async def set_balance(self, ctx: commands.Context, member: discord.Member, amount: int):
        sharkbot_member = SharkBot.Member.get(member.id)
        sharkbot_member.balance = amount
        await ctx.reply(f"Set {member.display_name}'s balance to ${amount}.")


async def setup(bot):
    await bot.add_cog(Economy(bot))
    print("Economy Cog Loaded.")


async def teardown(bot):
    await bot.remove_cog("Economy")
    print("Economy Cog Unloaded.")
