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


# ===== Cogs =====


@bot.command()
@commands.is_owner()
async def load(message, extension):
    await bot.load_extension(f"cogs.{extension.lower()}")
    await message.channel.send(f"{extension.capitalize()} Cog loaded.")


@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    extension = extension.lower()

    if extension == "all":
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                ext = filename[:-3]
                await ctx.invoke(bot.get_command("unload"), extension=ext)
        return

    await bot.unload_extension(f"cogs.{extension.lower()}")
    await ctx.reply(f"{extension.capitalize()} unloaded.")


@bot.command()
@commands.is_owner()
async def reload(ctx, extension="all"):
    extension = extension.lower()

    if extension == "all":
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                ext = filename[:-3]
                await bot.unload_extension(f"cogs.{ext}")
                await bot.load_extension(f"cogs.{ext}")
                await ctx.send(f"{ext.capitalize()} reloaded.")
                print(f"{ext.capitalize()} Cog reloaded.")
    else:
        await bot.unload_extension(f"cogs.{extension}")
        await bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"{extension.capitalize()} reloaded.")
        print(f"{extension.capitalize()} Cog reloaded.")


# ===== Main =====


async def main():
    print(colorama.Fore.CYAN + "\nStarting SharkBot main()...")

    print(colorama.Fore.CYAN + "\nLoading Cogs...\n")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
    print(colorama.Fore.GREEN + f"\nFinished loading Cogs.")

    print(colorama.Fore.CYAN + "\nStarting SharkBot...")
    async with bot:
        await bot.start(os.environ.get("DISCORD_TOKEN"))

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print(colorama.Fore.RED + "SharkBot Suspended - KeyboardInterrupt")
