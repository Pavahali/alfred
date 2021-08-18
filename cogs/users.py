from datetime import datetime as dt
from discord.ext import commands
import aiosqlite
import settings
import discord


class users(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["ктопнул"])
    async def whopinged(self, ctx):
        user = ''
        async with aiosqlite.connect(settings.db) as db:
            async with db.execute(
                    "SELECT lastpings FROM users WHERE id = ?" (ctx.author.id,)) as cursor:
                async for row in cursor:
                    user = row[0].split(';')

        embed = discord.Embed(title="Кто пнул")

        if user:
            out = ''
            for ping in user:
                out += f'\n<@{ping}>'
            embed.add_field(name=f'Пинги {ctx.author.name}', value=out)
        else:
            embed.add_field(name='Всё пусто', value='Тут ничего няма')

        await ctx.reply(embed=embed, mention_author=False)


def setup(bot):
    bot.add_cog(users(bot))
