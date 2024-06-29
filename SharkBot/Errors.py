import discord
from discord.ext import commands


class SharkError(Exception):

    async def report(self, ctx: commands.Context):
        return

    async def handler(self, ctx: commands.Context) -> bool:
        return False