import asyncio
import os
import subprocess
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


# ===== Core Commands =====

@bot.command()
@commands.is_owner()
async def update(ctx):

    try:
        os.chdir('/root/SharkBot')

        pull_result = subprocess.check_output(["git", "pull"]).decode('utf-8')
        pull_result_lines = pull_result.split("\n")
        pull_result_blocks: list[str] = [""]
        for line in pull_result_lines:
            if len(pull_result_blocks[-1]) + len(line) > 4000:
                pull_result_blocks[-1] = pull_result_blocks[-1][:-2]
                pull_result_blocks.append(line)
            else:
                pull_result_blocks[-1] += line + "\n"
        for block in pull_result_blocks:
            await ctx.send(embed=discord.Embed(
                title="Git Pull",
                description=f"```{block}```"
            ))

        restart_result = subprocess.check_output(["pm2", "restart", "sharkbot"]).decode('utf-8')
    except subprocess.CalledProcessError as e:
        await ctx.send(f"Update failed! Error: {e.returncode} - {e.output.decode('utf-8')}")
    except Exception as e:
        await ctx.send(f"An unexpected error occurred: {e}")


# ===== Main =====


async def main():

    async with bot:
        await bot.start(os.environ.get("DISCORD_TOKEN"))

asyncio.run(main())
