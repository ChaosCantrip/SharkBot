from datetime import datetime

import discord
import humanize
from discord.ext import commands
import SharkBot
import string

shop_ids: dict[SharkBot.Shop.ShopCategory, dict[str, SharkBot.Shop.ShopItem]] = {}
shop_items: dict[str, SharkBot.Shop.ShopItem] = {}

for _category_index, _category in enumerate(SharkBot.Shop.SHOP):
    shop_ids[_category] = {}
    for _item_index, _item in enumerate(_category.items):
        letter = string.ascii_lowercase[_item_index]
        shop_ids[_category][f"{_category_index + 1}{letter}"] = _item
        shop_items[f"{_category_index + 1}{letter}"] = _item


class Shop(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def shop(self, ctx: commands.Context):
        member = SharkBot.Member.get(ctx.author.id)
        if member.shop_data.needs_reset:
            member.shop_data.reset()
        embed = discord.Embed()
        embed.title = "Shop"
        embed.description = "Here are the items available in the shop.\nUse `$buy <id>` to buy an item.\n"
        embed.colour = discord.Colour.gold()
        for category, items in shop_ids.items():
            embed.add_field(
                name=category.name,
                value=f"*{category.description}*\n" + "\n".join([f"`{item_id}` Buy **{item.item}** for **{item.cost}**  ({item.limit - member.shop_data.get_times_bought(item_id)} Remaining)" for item_id, item in items.items()]),
                inline=False
            )
        reset_time_remaining = member.shop_data.reset_date - datetime.utcnow()
        embed.set_footer(text=f"Shop resets in {humanize.naturaldelta(reset_time_remaining)}")
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Shop(bot))
    print("Shop Cog Loaded.")


async def teardown(bot):
    await bot.remove_cog("Shop")
    print("Shop Cog Unloaded.")
