from discord.ext import commands
from pyfiglet import Figlet
import asyncio
import discord


class comms(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = 1):
        amount = (lambda x: 1 if x <= 0 else 100 if x
                  >= 101 else x)(amount + 1)
        await ctx.channel.purge(limit=amount)
        message = await ctx.send(f"Удалено {amount} сообщений")
        await asyncio.sleep(10)
        await message.delete()

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

    @commands.command(aliases=["moodyblues", "repeat"])
    async def echo(self, ctx, *, msg=''):
        await ctx.send(msg, allowed_mentions=discord.AllowedMentions(
            everyone=False,
            users=False,
            roles=False))


def setup(bot):
    bot.add_cog(comms(bot))
