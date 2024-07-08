import discord
from discord.ext import commands


class SharkError(Exception):
    """Base class for all custom SharkBot Errors"""

    async def report(self, ctx: commands.Context):
        """Method for reporting error to developer"""

        return

    async def handler(self, ctx: commands.Context) -> bool:
        """Method for responding to the invoking command with a coherent response"""

        return False

class LootpoolNotFoundError(SharkError):
    pass