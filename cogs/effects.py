import discord
from discord.ext import tasks, commands
from definitions import Member, Effect, SharkErrors
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
    async def addeffect(self, ctx, targetMember: discord.Member, effectid: int, rawduration: int):
        member = Member.get(targetMember.id)
        effect = Effect.get(effectid)
        if rawduration == 0:
            duration = None
        else:
            duration = timedelta(seconds=rawduration)
        member.apply_effect(effect, duration)
        await ctx.send(f"Applied **{effect.name}** to *{targetMember.display_name}*")

    @commands.command()
    @commands.has_role(ids.roles["Mod"])
    async def removeeffect(self, ctx, targetMember: discord.Member, effectid: int):
        member = Member.get(targetMember.id)
        effect = Effect.get(effectid)
        try:
            member.remove_effect(effect)
            await ctx.send(f"Removed **{effect.name}** effect from *{targetMember.display_name}*")
        except SharkErrors.EffectNotAppliedError:
            await ctx.send(f"*{targetMember.display_name}* doesn't have **{effect.name}** applied!")



def setup(bot):
    bot.add_cog(Effects(bot))
    print("Effects Cog loaded")


def teardown(bot):
    print("Effects Cog unloaded")
    bot.remove_cog(Effects(bot))
