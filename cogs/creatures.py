import discord
from discord.ext import commands
import SharkBot


class Creatures(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @SharkBot.Checks.Permissions.is_admin()
    async def admin_add_power(self, ctx: commands.Context, member: discord.Member, base_creature_id: str, power: int):
        sharkbot_member = SharkBot.Member.get(member.id)
        over_power = sharkbot_member.creatures.add_power(base_creature_id, power)
        sharkbot_member.write_data()
        await ctx.send(f"{member.mention}'s `{base_creature_id}` has gained {power} power. {over_power} power was lost.")

    @commands.command()
    async def creature(self, ctx: commands.Context, *, search):
        member = SharkBot.Member.get(ctx.author.id)
        creature = SharkBot.Creature.search(search)
        try:
            member_creature = member.creatures.get(creature.id)
        except SharkBot.Errors.CreatureNotFoundError:
            await ctx.send(f"You do not have a `{creature.id}`.")
            return
        embed = discord.Embed()
        embed.title = f"{ctx.author.display_name}'s {creature.name}"
        embed.description = f"{member_creature.power}P | Level {member_creature.level}"
        embed.add_field(
            name="Stats",
            value=f"Attack:                   `{member_creature.stats.attack}`\n"
                  f"Defense:                  `{member_creature.stats.defense}`\n"
                  f"Max HP:                   `{member_creature.stats.max_health}`\n"
                  f"Critical Chance:          `{member_creature.stats.critical_chance:.2%}`\n"
                  f"Evade Chance:             `{member_creature.stats.evade_chance:.2%}`\n"
                  f"Additional Attack Chance: `{member_creature.stats.additional_attack_chance:.2%}`\n",
            inline=False
        )
        embed.colour = member_creature.alignment.colour
        embed.set_thumbnail(url=creature.icon_url)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Creatures(bot))
    print("Creatures Cog Loaded.")


async def teardown(bot):
    await bot.remove_cog("Creatures")
    print("Creatures Cog Unloaded.")
