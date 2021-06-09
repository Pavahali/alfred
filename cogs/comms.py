from discord.ext import commands
from pyfiglet import Figlet
from cogs import logs
from cogs import db
import discord



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

    @commands.command()
    async def ascii(self, ctx, *, text):
        if text.isascii():
            out = Figlet(font='big').renderText(text)
            if len(out) >= 1000:
                await ctx.send('Слишком большое сообщение')
            else:
                await ctx.send("```\n" + out + "\n```")
        else:
            await ctx.send('Только ascii!')

    @commands.command(aliases=["repeat"])
    async def echo(self, ctx, *, msg=''):
        await ctx.send(msg, allowed_mentions=discord.AllowedMentions(everyone=False, users=False, roles=False))

def setup(bot):
    bot.add_cog(comms(bot))
