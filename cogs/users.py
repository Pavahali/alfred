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
                    "SELECT lastpings FROM users WHERE id = ?", (ctx.author.id,)) as cursor:
                async for row in cursor:
                    user = row[0].split(';')
                    count = 0
                    for ping in user:
                        user[count] = ping.split('.')
                        count += 1

        embed = discord.Embed(title="Кто пнул")

        if user:
            out = ''
            for ping in user:
                try:
                    msg = await ctx.fetch_message(int(ping[2]))
                    msg = f'([перейти]({msg.jump_url}))'
                except:
                    msg = '(сообщение удалено)'

                out += f'\n<@{ping[0]}> <t:{ping[1]}:R> {msg}'
            embed.add_field(name=f'Пинги {ctx.author.name}', value=out)
        else:
            embed.add_field(name='Всё пусто', value='Тут ничего няма')

        await ctx.reply(embed=embed, mention_author=False)


def setup(bot):
    bot.add_cog(users(bot))
