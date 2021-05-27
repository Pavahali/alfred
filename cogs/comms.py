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

        embed=discord.Embed(title="История пингов", description=f"История пингов {ctx.author}")
        if pings[2] != '-':
            embed.add_field(name=" ", value=pings[2], inline=False)
        else:
            embed.add_field(name=" ", value="Никто не пинговал")
        if pings[1] != '-':
            embed.add_field(name=" ", value=pings[1], inline=False)
        if pings[0] != '-':
            embed.add_field(name=" ", value=pings[0], inline=False)
        await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(comms(bot))
