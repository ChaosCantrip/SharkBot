import discord
from discord.ext import commands

import SharkBot


import logging

cog_logger = logging.getLogger("cog")

class Levels(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.hybrid_command()
    async def level(self, ctx: commands.Context):
        member = SharkBot.Member.get(ctx.author.id, discord_user=ctx.author)

        embed = discord.Embed()
        embed.title = f"{ctx.author.display_name}'s Level"
        embed.set_thumbnail(url=ctx.author.display_avatar.url)
        embed.description = f"You are **Level {member.xp.level}** with `{member.xp.xp:,} xp`"

        embed.add_field(
            name=f"XP to Level {member.xp.level + 1}",
            value=f"`{member.xp.xp_to_next:,} xp` to go"
        )

        await ctx.reply(embed=embed)

    @commands.command()
    @SharkBot.Checks.is_mod()
    async def add_xp(self, ctx: commands.Context, target: discord.Member, amount: int):
        target_member = SharkBot.Member.get(target.id)
        await target_member.xp.add(amount, ctx)
        await ctx.reply(f"Added `{amount:,} xp` to {target.mention}")

    @commands.command()
    @SharkBot.Checks.is_mod()
    async def set_xp(self, ctx: commands.Context, target: discord.Member, amount: int, give_rewards: int = 1):
        target_member = SharkBot.Member.get(target.id)
        await target_member.xp.set(amount, ctx, True if give_rewards == 1 else False)
        await ctx.reply(f"Set {target.mention} to `{amount:,} xp`")

    @commands.command()
    @commands.is_owner()
    async def initialise_xp(self, ctx: commands.Context):
        for member in SharkBot.Member.members:
            amount = 0
            amount += member.collection.xp_value
            amount += 3 * member.stats.completed_missions
            amount += member.counts
            await member.xp.set(amount, ctx)

        output = "\n".join(f"{member.id} | {member.xp.xp} | {member.xp.level}" for member in SharkBot.Member.members)

        await ctx.reply(output)

    @commands.hybrid_command()
    async def get_level(self, ctx: commands.Context, target: discord.Member):
        member = SharkBot.Member.get(target.id)

        embed = discord.Embed()
        embed.title = f"{target.display_name}'s Level"
        embed.set_thumbnail(url=target.display_avatar.url)
        embed.description = f"{target.mention} is **Level {member.xp.level}** with `{member.xp.xp:,} xp`"

        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Levels(bot))
    print("Levels Cog Loaded")
    cog_logger.info("Levels Cog Loaded")


async def teardown(bot):
    await bot.remove_cog(Levels(bot))
    print("Levels Cog Unloaded")
    cog_logger.info("Levels Cog Unloaded")