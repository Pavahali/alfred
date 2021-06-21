from discord.ext import commands
from datetime import datetime as dt
from cogs import db
import discord


class users(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx, userid=''):
        if not ctx.message.mentions:
            user = await self.bot.fetch_user(userid)
            if not user:
                await ctx.send("Нужно указать айдишник или пингануть юзера")
        else:
            user = ctx.message.mentions[0]

        info = await db.ruser(user.id)

        pings = []
        for i in info["userpings"]:
            if i["id"] != 0:
                j = await self.bot.fetch_user(int(i["id"]))
                pings.append([str(j), dt.fromtimestamp(i["time"]).strftime("%H:%M %d/%m/%y")])
            else:
                pings.append('-')

        userpings = ""
        if pings[2][0] != '-':
            for i in pings:
                if i[0] != '-':
                    userpings += "\n" + i[0] + " at " + i[1]
        else:
            userpings = "В бд пусто"
        embed=discord.Embed(title="Инфа о юзере", description=user)
        embed.add_field(name="Бот?", value=user.bot, inline=True)
        embed.add_field(name="Дата создания акка", value=user.created_at, inline=True)
        embed.add_field(name="Айдишник", value=user.id, inline=True)
        embed.add_field(name="Пинги", value=userpings, inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(users(bot))
