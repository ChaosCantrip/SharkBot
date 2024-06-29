import asyncio
import os
import colorama
import discord
from discord.ext import commands

colorama.init(autoreset=True)

import SharkBot

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all(), case_insensitive=True)


@bot.event
async def on_ready():
    print(colorama.Fore.GREEN + "SharkBot connected to Discord")
    print(colorama.Fore.YELLOW + f"\t- Account: {bot.user}")
    print(colorama.Fore.YELLOW + f"\t- User ID: {bot.user.id}")

    embed = discord.Embed()
    embed.title = "SharkBot is up and running!"
    embed.description = "SharkBot is now connected to Discord."
    embed.set_thumbnail(url=bot.user.display_avatar.url)
    embed.colour = discord.Colour.green()

    app_info = await bot.application_info()
    owner = app_info.owner
    await owner.send(embed=embed)
    await bot.change_presence(status=discord.Status.online)


# ===== Main =====


async def main():

    async with bot:
        await bot.start(os.environ.get("DISCORD_TOKEN"))

asyncio.run(main())
