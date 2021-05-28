from discord.ext import commands
from cogs import logs
import discord
from cogs import db



class comms(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["ктопнул"])
    async def whopinged(self, ctx):
        user = await db.ruser(ctx.author.id)

        pings = []
        for i in user["lastpings"]:
            if i != "-":
                j = await self.bot.fetch_user(int(i))
                pings.append(str(j))
            else:
                pings.append('-')

        desc = f"История пингов {ctx.author}:"
        if pings[2] != '-':
            desc += "\n" + pings[2]
        else:
            desc = "Никто не пинговал"
        if pings[1] != '-':
            desc += "\n" + pings[1]
        if pings[0] != '-':
            desc += "\n" + pings[0]
        embed=discord.Embed(title="Кто пнул", description=desc)
        await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
    bot.add_cog(comms(bot))
