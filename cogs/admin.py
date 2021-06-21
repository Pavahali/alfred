from discord.ext import commands
from cogs import logs
from cogs import db
import subprocess
import discord

class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command()
    async def reload(self, ctx, cog):
        self.bot.unload_extension(f'cogs.{cog}')
        self.bot.load_extension(f'cogs.{cog}')

        await ctx.send(f'{cog} перезагружен')
        logs.log(f'{cog} reloaded','0')

    @commands.is_owner()
    @commands.command()
    async def load(self, ctx, cog):
        self.bot.load_extension(f'cogs.{cog}')

        await ctx.send(f'{cog} подгрузился')
        logs.log(f'{cog} enabled','0')

    @commands.is_owner()
    @commands.command()
    async def unload(self, ctx, cog):
        self.bot.unload_extension(f'cogs.{cog}')

        await ctx.send(f'{cog} выключен')
        logs.log(f'{cog} disabled', '0')

    @commands.is_owner()
    @commands.command()
    async def changedb(self, ctx, action, userid, msg=''):
        if action.lower() in ["del", "rem", "delete", "remove"]:
            await db.duser(userid)
            await ctx.send(f'Юзер с айдишником {userid} был удалён')

        elif action.lower() in ["read", "get"]:
            user = await db.ruser(userid)
            await ctx.send('```\n'+str(user).replace(',', ',\n')+'\n```')

        else:
            await ctx.send('Еблан, не то действие!')


def setup(bot):
    bot.add_cog(admin(bot))
