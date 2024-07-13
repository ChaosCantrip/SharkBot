import discord
from discord.ext import commands
import SharkBot
import string

active_banners: dict[SharkBot.Banner, dict[str, SharkBot.BuyOption]] = {}

for _banner_index, _banner in enumerate(SharkBot.Banner.get_active_banners()):
    active_banners[_banner] = {}
    for _buy_option_index, _buy_option in enumerate(_banner.buy_options):
        letter = string.ascii_lowercase[_buy_option_index]
        active_banners[_banner][f"{_banner_index + 1}{letter}"] = _buy_option


class Banners(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def banners(self, ctx: commands.Context):
        embed = discord.Embed()
        embed.title = "Banners"
        embed.description = "Here are the currently active banners.\nUse `$pull <id>` to pull from a banner.\n"
        for banner, buy_options in active_banners.items():
            embed.add_field(
                name=banner.name,
                value=f"*{banner.description}*\n" + "\n".join([f"`{option_id}` {buy_option.name} - {buy_option.cost}" for option_id, buy_option in buy_options.items()]),
                inline=False
            )
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Banners(bot))
    print("Banners Cog Loaded.")


async def teardown(bot):
    await bot.remove_cog("Banners")
    print("Banners Cog Unloaded.")
