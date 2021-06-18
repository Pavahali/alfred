from discord.ext import commands
from cogs import logs
from cogs import db
import subprocess
import discord
import pprint

class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command()
    async def reload(self, ctx, cog):
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
        result = subprocess.run(exec.split(' '), stdout=subprocess.PIPE).stdout.decode('utf-8')
        await ctx.send(f"```{result}```")

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
