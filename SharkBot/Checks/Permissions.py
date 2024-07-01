import discord
from discord.ext import commands
import SharkBot


def is_admin():
    async def predicate(ctx: commands.Context):
        member = SharkBot.Member.get(ctx.author.id)
        if member.permissions.admin:
            return True
        app_info = await ctx.bot.application_info()
        if ctx.author.id == app_info.owner.id:
            return True
        raise commands.MissingPermissions(["admin"])
    return commands.check(predicate)
