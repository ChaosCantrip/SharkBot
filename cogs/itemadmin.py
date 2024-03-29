import discord
from discord.ext import commands

import SharkBot


import logging

cog_logger = logging.getLogger("cog")

class ItemAdmin(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @SharkBot.Checks.is_mod()
    async def add_item(self, ctx: commands.Context, target: discord.Member, *, search: str) -> None:
        target_member = SharkBot.Member.get(target.id)
        try:
            item = SharkBot.Item.search(search)
        except SharkBot.Errors.ItemNotFoundError:
            await ctx.reply("Sorry, I couldn't find that item!", mention_author=False)
            return
        response = target_member.inventory.add(item)
        await ctx.reply(f"Added **{str(response)}** to *{target.display_name}*'s inventory.", mention_author=False)
        target_member.write_data()

    @commands.command()
    @SharkBot.Checks.is_mod()
    async def remove_item(self, ctx: commands.Context, target: discord.Member, *, search: str) -> None:
        target_member = SharkBot.Member.get(target.id)
        try:
            item = SharkBot.Item.search(search)
        except SharkBot.Errors.ItemNotFoundError:
            await ctx.reply("Sorry, I couldn't find that item!", mention_author=False)
            return
        try:
            target_member.inventory.remove(item)
        except SharkBot.Errors.ItemNotInInventoryError:
            await ctx.reply(f"Couldn't find item in *{target.display_name}*'s inventory", mention_author=False)
            return
        await ctx.reply(f"Removed **{item.name}** from *{target.display_name}*'s inventory.", mention_author=False)
        target_member.write_data()

    @commands.command()
    @SharkBot.Checks.is_mod()
    async def grant_all(self, ctx: commands.Context, *itemids: str) -> None:
        items: list[SharkBot.Item.Item] = [SharkBot.Item.get(itemid) for itemid in itemids]
        item_types: set[SharkBot.Item.Item] = set(items)

        members = SharkBot.Member.members
        for member in members:
            member.inventory.add_items(items)

        embed = discord.Embed()
        embed.title = "Grant All"
        embed.description = f"Granted `{len(items)} Items` to each of `{len(members)} Members`."
        embed.add_field(
            name="Items Granted",
            value="\n".join(f"{items.count(item)}x **{item}**" for item in item_types),
            inline=False
        )

        for e in SharkBot.Utils.split_embeds(embed):
            await ctx.reply(embed=e, mention_author=False)

        for member in members:
            member.write_data()


async def setup(bot):
    await bot.add_cog(ItemAdmin(bot))
    print("ItemAdmin Cog Loaded")
    cog_logger.info("ItemAdmin Cog Loaded")


async def teardown(bot):
    await bot.remove_cog(ItemAdmin(bot))
    print("ItemAdmin Cog Unloaded")
    cog_logger.info("ItemAdmin Cog Unloaded")