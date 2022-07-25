import discord
from discord.ext import tasks, commands
from definitions import Member, Effect
from datetime import timedelta

import secret

if secret.testBot:
    import testids as ids
else:
    import ids


class Effects(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def effects(self, ctx):
        member = Member.get(ctx.author.id)
        if len(member.effects) == 0:
            await ctx.send("You have no effects applied!")
        for effect in member.get_effects():
            await ctx.send(f"ID: {effect.effect.id}, Name: {effect.effect.name}, Expiry: {effect.get_expiry_text()}")

    @commands.command()
    @commands.has_role(ids.roles["Mod"])
    async def addeffect(self, ctx, discordMember: discord.Member, effectid: int, rawduration: int):
        member = Member.get(discordMember.id)
        effect = Effect.get(effectid)
        if rawduration == 0:
            duration = None
        else:
            duration = timedelta(seconds=rawduration)
        member.apply_effect(effect, duration)
        await ctx.send(f"Applied **{effect.name}** to *{discordMember.display_name}*")



def setup(bot):
    bot.add_cog(Effects(bot))
    print("Effects Cog loaded")


def teardown(bot):
    print("Effects Cog unloaded")
    bot.remove_cog(Effects(bot))
