from discord.ext import commands
from exts import logs
from exts import db
import subprocess
import settings
import discord
import os


class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command()
    async def reload(self, ctx, cog):
        self.bot.unload_extension(f'cogs.{cog}')
        self.bot.load_extension(f'cogs.{cog}')

        await ctx.send(f'{cog} перезагружен')
        logs.log(f'{cog} reloaded','1')

    @commands.is_owner()
    @commands.command()
    async def load(self, ctx, cog):
        self.bot.load_extension(f'cogs.{cog}')

        await ctx.send(f'{cog} подгрузился')
        logs.log(f'{cog} enabled','1')

    @commands.is_owner()
    @commands.command()
    async def unload(self, ctx, cog):
        self.bot.unload_extension(f'cogs.{cog}')

        await ctx.send(f'{cog} выключен')
        logs.log(f'{cog} disabled', '1')

    @commands.is_owner()
    @commands.command()
    async def shutdown(self, ctx):
        await ctx.send("Пока!")
        logs.log(f'Shutting down...', '1')
        exit()
        
def setup(bot):
    bot.add_cog(admin(bot))
