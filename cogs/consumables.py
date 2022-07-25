import discord
from discord.ext import tasks, commands
from definitions import Member, Item

import secret

if secret.testBot:
    import testids as ids
else:
    import ids


class Consumables(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def use(self, ctx, *, search):
        member = Member.get(ctx.author.id)
        item = Item.search(search)

        if type(item) is not Item.ConsumableItem:
            await ctx.send(f"**{item.name}** is not a consumable item!")
            return

        if item.id not in member.get_inventory():
            await ctx.send(f"You don't have a **{item.name}**!")
            return

        member.apply_effect(item.effect, item.effectduration)
        member.remove_from_inventory(item)
        await ctx.send(f"You used a **{item.name}**!")



def setup(bot):
    bot.add_cog(Consumables(bot))
    print("Consumables Cog loaded")


def teardown(bot):
    print("Consumables Cog unloaded")
    bot.remove_cog(Consumables(bot))
