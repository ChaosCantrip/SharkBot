import discord
from discord.ext import commands
import SharkBot


def is_admin():
    async def predicate(ctx: commands.Context):
        member = SharkBot.Member.get(ctx.author.id)
        if not member.permissions.admin:
            raise commands.MissingPermissions(["admin"])
    return commands.check(predicate)
