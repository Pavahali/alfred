from discord.ext import commands
from cogs import logs
import subprocess
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

    @commands.is_owner()
    @commands.command()
    async def shell(self, ctx, *, exec):
    result = subprocess.run(exec, stdout=subprocess.PIPE)
    await ctx.send(result.stdout)

def setup(bot):
    bot.add_cog(admin(bot))
