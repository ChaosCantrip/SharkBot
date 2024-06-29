import asyncio
import os

import discord
from discord.ext import commands

import SharkBot

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all(), case_insensitive=True)


@bot.event
async def on_ready():
    print("Bot is ready")
    app_info = await bot.application_info()
    owner = app_info.owner
    await owner.send("SharkBot up and running!")


# ===== Main =====


async def main():

    async with bot:
        await bot.start(os.environ.get("DISCORD_TOKEN"))

asyncio.run(main())
