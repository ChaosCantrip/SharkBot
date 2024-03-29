import logging
from datetime import datetime, time

import discord
from discord.ext import tasks, commands

import SharkBot

cog_logger = logging.getLogger("cog")

class Database(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.database_loop.start()
        self.reset_loop.start()
        self.total_uploads = 0

    def cog_unload(self) -> None:
        self.database_loop.cancel()
        self.reset_loop.cancel()

    @tasks.loop(time=[time(hour=0)])
    async def reset_loop(self):
        self.total_uploads = 0

    @reset_loop.error
    async def reset_loop_error(self, error: Exception):
        await SharkBot.Utils.task_loop_handler(self.bot, error)

    @tasks.loop(time=[time(hour=i) for i in range(0,23)])
    async def database_loop(self):
        messages = []
        for member in SharkBot.Member.members:
            await member.fetch_discord_user(self.bot)
            if member.snapshot.has_changed:
                messages.append(member.upload_data(force_upload=True))

        changed_members = [member for member in SharkBot.Member.members if member.times_uploaded > 0]
        if len(changed_members) > 0:
            messages.append("\nCompleted Uploads in the last hour:")
        for member in changed_members:
            if member.discord_user is not None:
                member_name = f"{member.discord_user.display_name}#{member.discord_user.discriminator}"
            else:
                member_name = str(member.id)
            messages.append(f"{member_name} - {member.times_uploaded}")
            self.total_uploads += member.times_uploaded
            member.times_uploaded = 0

        if len(messages) > 0:
            embed = discord.Embed()
            embed.title = "Database Update"
            embed.description = f"<t:{int(datetime.now().timestamp())}:D>\n"
            embed.description += "```" + "\n".join(messages) + "```"
            embed.set_footer(text=f"Total Uploads Today: {self.total_uploads}")

            db_log_channel = await self.bot.fetch_channel(SharkBot.IDs.channels["Database Log"])
            await db_log_channel.send(embed=embed)


    @database_loop.before_loop
    async def before_update(self):
        await self.bot.wait_until_ready()

    @database_loop.error
    async def update_db_error(self, error: Exception):
        await SharkBot.Utils.task_loop_handler(self.bot, error)

    @commands.command()
    @commands.is_owner()
    async def force_upload(self, ctx: commands.Context, target: discord.Member):
        member = SharkBot.Member.get(target.id)
        await member.fetch_discord_user(self.bot)
        message = await ctx.reply(f"Uploading data for {target.mention}...")
        response = member.upload_data(force_upload=True)
        await message.edit(content=message.content + f"'{response}'")

    @commands.command()
    @commands.is_owner()
    async def force_upload_all(self, ctx: commands.Context):
        num = len(SharkBot.Member.members)
        message = await ctx.reply(f"Uploading all member data for `{num}` Members...")
        failures = []
        for i, member in enumerate(SharkBot.Member.members):
            response = member.upload_data(force_upload=True)
            if not response.startswith("Success"):
                failures.append(member)
        if len(failures) == 0:
            await message.edit(content=f"Uploaded all member data for `{num}` members.")
        else:
            await message.edit(content=f"Uploaded data for `{num - len(failures)}/{num}` members. Retrying for `{len(failures)}` Members...")
            full_failures = []
            for i, member in enumerate(failures):
                await member.fetch_discord_user(self.bot)
                response = member.upload_data(force_upload=True)
                if not response.startswith("Success"):
                    full_failures.append(member)
            if len(full_failures) == 0:
                await message.edit(content=f"Uploaded all member data for {num} members.")
            else:
                content = f"Uploaded data for {num - len(full_failures)}/{num} members.\n"
                content += f"{len(full_failures)} fully failed to upload.\n\n"
                content += "\n".join(f"{m_id} - <@{m_id}>" for m_id in full_failures)
                await message.edit(content=content)


async def setup(bot):
    await bot.add_cog(Database(bot))
    print("Database Cog Loaded")
    cog_logger.info("Database Cog Loaded")


async def teardown(bot):
    await bot.remove_cog(Database(bot))
    print("Database Cog Unloaded")
    cog_logger.info("Database Cog Unloaded")