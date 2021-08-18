from discord.ext import commands
import aiosqlite
import settings
import discord


class status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def guildinfo(self, ctx):
        async with aiosqlite.connect(settings.db) as db:
            guild = ()
            async with db.execute(
                    "SELECT botchannel, isenabled FROM guilds WHERE id = ?", (ctx.guild.id,)) as cursor:
                async for row in cursor:
                    guild = row
            if not guild:
                await db.execute("INSERT INTO guilds(id) VALUES(?)",
                                 (ctx.guild.id,))
                await db.commit()
                guild = (0, 0)
        try:
            name = await self.bot.fetch_channel(guild[0]).name
        except:
            name = "None"

        embed = discord.Embed(title='Инфа о сервере')
        embed.add_field(name='Канал для команд',
                        value=name, inline=False)
        embed.add_field(name='Игнорить пинги?', value=bool(guild[1]))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(status(bot))
