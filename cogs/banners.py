import discord
from discord.ext import commands
import SharkBot
import string

active_banners: dict[SharkBot.Banner, dict[str, SharkBot.BuyOption]] = {}
active_buy_options: dict[str, tuple[SharkBot.Banner, SharkBot.BuyOption]] = {}

for _banner_index, _banner in enumerate(SharkBot.Banner.get_active_banners()):
    active_banners[_banner] = {}
    for _buy_option_index, _buy_option in enumerate(_banner.buy_options):
        letter = string.ascii_lowercase[_buy_option_index]
        active_banners[_banner][f"{_banner_index + 1}{letter}"] = _buy_option
        active_buy_options[f"{_banner_index + 1}{letter}"] = (_banner, _buy_option)


class Banners(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @SharkBot.Checks.Permissions.is_admin()
    async def admin_add_tickets(self, ctx: commands.Context, target_member: discord.Member, ticket_id: str, amount: int):
        member = SharkBot.Member.get(target_member.id)
        ticket = SharkBot.Ticket.get(ticket_id.lower())
        member.tickets.add_tickets(ticket, amount)
        member.write_data()
        await ctx.reply(f"Added {amount}x **{ticket.name}** to {target_member.mention}'s inventory")

    @commands.command()
    async def banners(self, ctx: commands.Context):
        embed = discord.Embed()
        embed.title = "Banners"
        embed.description = "Here are the currently active banners.\nUse `$pull <id>` to pull from a banner.\n"
        for banner, buy_options in active_banners.items():
            embed.add_field(
                name=banner.name,
                value=f"*{banner.description}*\n" + "\n".join([f"`{option_id}` {buy_option.name} - {buy_option.cost}" for option_id, buy_option in buy_options.items()]),
                inline=False
            )
        await ctx.send(embed=embed)

    @commands.command()
    async def pull(self, ctx: commands.Context, banner_id: str):
        member = SharkBot.Member.get(ctx.author.id)
        banner_id = banner_id.lower()
        embed = discord.Embed()
        embed.title = f"{ctx.author.display_name}'s Pull"
        if banner_id not in active_buy_options:
            embed.colour = discord.Colour.red()
            embed.description = "Invalid banner ID."
            await ctx.send(embed=embed)
            return
        banner, buy_option = active_buy_options[banner_id]
        if type(buy_option.cost) == SharkBot.TicketCost:
            try:
                member.tickets.remove_tickets(buy_option.cost.ticket, buy_option.cost.amount)
            except SharkBot.Errors.NotEnoughTicketsError:
                embed.colour = discord.Colour.red()
                embed.description = f"You only have {member.tickets.tickets.count(buy_option.cost.ticket)}x :ticket: **{buy_option.cost.ticket.name}**"
                await ctx.send(embed=embed)
                return
        embed.description = f"You pulled `{sum([pull.number for pull in buy_option.pulls])}x` from the **{banner.name}**."
        embed.description += "\n" + "\n".join([f"{pull.number}x {pull.lootpool_id}" for pull in buy_option.pulls])
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Banners(bot))
    print("Banners Cog Loaded.")


async def teardown(bot):
    await bot.remove_cog("Banners")
    print("Banners Cog Unloaded.")
