from discord.ext import commands
from cogs import logs
import discord

class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command()
    async def unload(self, ctx, cog):
        self.bot.unload_extension(f'cogs.{cog}')
        self.bot.load_extension(f'cogs.{cog}')
        await ctx.send(f'{cog} перезагружен')
        print(f'Перезагружен ког {cog}')
        logs.log(f'{cog} reloaded','0')

    @commands.is_owner()
    @commands.command()
    async def load(self, ctx, cog):
        self.bot.load_extension(f'cogs.{cog}')
        await ctx.send(f'{cog} подгрузился')
        print(f'Включен ког {cog}')
        logs.log(f'{cog} enabled','0')

    @commands.is_owner()
    @commands.command()
    async def unload(self, ctx, cog):
        self.bot.unload_extension(f'cogs.{cog}')
        await ctx.send(f'{cog} выключен')
        print(f'Выключен ког {cog}')
        logs.log(f'{cog} disabled', '0')

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        channel = self.bot.get_channel(618044439939645444)
        await channel.send('Я выключаюсь...')
        log(f'Turning off...', '1')
        await self.bot.logout()


def setup(bot):
    bot.add_cog(admin(bot))
