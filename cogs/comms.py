from discord.ext import commands
from cogs import logs
import discord
from cogs import logs
from cogs import db



class comms(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["ктопнул"])
    async def whopinged(self, ctx):
        user = db.ruser(ctx.author.id)

        pings = []
        for i in user["lastpings"]:
            if i != "-":
                j = await self.bot.fetch_user(int(i))
                pings.append(str(j))
            else:
                pings.append('-')

        embed=discord.Embed(title="Ктопнул", description=str(ctx.author))
        embed.add_field(name="1", value=pings[2], inline=False)
        embed.add_field(name="2", value=pings[1], inline=False)
        embed.add_field(name="3", value=pings[0], inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(comms(bot))
