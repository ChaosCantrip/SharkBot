import discord
from discord.ext import commands
import random
import SharkBot


class Fun(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(
        aliases=["cf"],
        brief="Bet an amount of SharkCoins on a coin flip to get double or nothing back!"
    )
    async def coinflip(self, ctx, amount: int) -> None:
        member = SharkBot.Member.get(ctx.author.id)
        embed = discord.Embed()
        embed.title = "Coin Flip"
        if ctx.author.id == 473172414688395274:
            embed.title = "Coin Flippies for Daddy Braddy Mullies"
        embed.description = f"You bet :dollar: **{amount:,}**!"
        embed.set_thumbnail(url="https://i.pinimg.com/originals/d7/49/06/d74906d39a1964e7d07555e7601b06ad.gif")

        if amount < 0:
            embed.colour = discord.Color.red()
            embed.add_field(
                name="Negative Bet!",
                value="You can't bet a negative amount of money!"
            )
            await ctx.reply(embed=embed)
            return

        if amount == 0:
            embed.colour = discord.Color.red()
            embed.add_field(
                name="Zero Bet!",
                value="You can't bet :dollar: **0**!!"
            )
            await ctx.reply(embed=embed)
            return

        if member.balance < amount:
            embed.colour = discord.Color.red()
            embed.add_field(
                name="Not Enough Money!",
                value=f"You only have :dollar: **{member.balance:,}**"
            )
            await ctx.reply(embed=embed)
            return

        roll = random.randint(1, 16)
        if roll <= 7:  # Win
            member.balance += amount
            embed.colour = discord.Color.green()
            embed.add_field(
                name="You win!",
                value=f"You won :dollar: **{amount:,}**!"
            )
        elif roll <= 9:  # Mercy Loss
            embed.colour = discord.Color.blurple()
            embed.add_field(
                name="You lose!",
                value=f"You lost, but I'm feeling nice, so I'll let you keep your money!"
            )
        else:  # Loss
            member.balance -= amount
            embed.colour = discord.Color.dark_red()
            embed.add_field(
                name="You lose!",
                value=f"You lost :dollar: **{amount:,}**!"
            )
        await ctx.reply(embed=embed)
        member.write_data()


async def setup(bot):
    await bot.add_cog(Fun(bot))
    print("Fun Cog Loaded.")


async def teardown(bot):
    await bot.remove_cog("Balance")
    print("Fun Cog Unloaded.")
