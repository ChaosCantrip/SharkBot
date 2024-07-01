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
        embed.description = f"Your balance is **${member.balance}**."
        embed.set_thumbnail(url=ctx.author.display_avatar.url)
        embed.colour = discord.Colour.gold()

        await ctx.reply(embed=embed)

    @commands.command()
    @SharkBot.Checks.Permissions.is_admin()
    async def add_balance(self, ctx: commands.Context, member: discord.Member, amount: int):
        sharkbot_member = SharkBot.Member.get(member.id)
        sharkbot_member.balance += amount
        await ctx.reply(f"Added ${amount} to {member.display_name}'s balance.")

    @commands.command()
    @SharkBot.Checks.Permissions.is_admin()
    async def set_balance(self, ctx: commands.Context, member: discord.Member, amount: int):
        sharkbot_member = SharkBot.Member.get(member.id)
        sharkbot_member.balance = amount
        await ctx.reply(f"Set {member.display_name}'s balance to ${amount}.")

    @commands.command()
    async def claim(self, ctx: commands.Context):
        member = SharkBot.Member.get(ctx.author.id)

        embed = discord.Embed()
        embed.title = f"{ctx.author.display_name}'s Claim"
        embed.colour = discord.Colour.blurple()
        embed.set_thumbnail(url=ctx.author.display_avatar.url)
        embed.description = "Free shit!"

        if member.cooldowns.hourly.expired:
            member.cooldowns.hourly.reset()
            member.balance += 10
            embed.add_field(
                name="Hourly",
                value="Success! You claimed **$10**!",
                inline=False
            )
        else:
            embed.add_field(
                name="Hourly",
                value=f"You still have *{member.cooldowns.hourly.time_remaining_string}* left!",
                inline=False
            )

        if member.cooldowns.daily.expired:
            member.cooldowns.daily.reset()
            member.balance += 100
            embed.add_field(
                name="Daily",
                value="Success! You claimed **$100**!",
                inline=False
            )
        else:
            embed.add_field(
                name="Daily",
                value=f"You still have *{member.cooldowns.daily.time_remaining_string}* left!",
                inline=False
            )

        if member.cooldowns.weekly.expired:
            member.cooldowns.weekly.reset()
            member.balance += 500
            embed.add_field(
                name="Weekly",
                value="Success! You claimed **$500**!",
                inline=False
            )
        else:
            embed.add_field(
                name="Weekly",
                value=f"You still have *{member.cooldowns.weekly.time_remaining_string}* left!",
                inline=False
            )

        await ctx.reply(embed=embed)
        member.write_data()

    @commands.command(aliases=["transfer"])
    async def pay(self, ctx, target: discord.Member, amount: int):
        member = SharkBot.Member.get(ctx.author.id)
        target_member = SharkBot.Member.get(target.id)

        if amount < 0:
            await ctx.send("Nice try buddy. Please enter a positive amount!")
            return
        if member.balance < amount:
            await ctx.send("Sorry, you don't have enough SharkCoins to do that.")
            return

        member.balance -= amount
        target_member.balance += amount
        await ctx.reply(f"Sent **${amount:,}** to {target.mention}.", mention_author=False)

        member.write_data()
        target_member.write_data()


async def setup(bot):
    await bot.add_cog(Economy(bot))
    print("Economy Cog Loaded.")


async def teardown(bot):
    await bot.remove_cog("Economy")
    print("Economy Cog Unloaded.")
