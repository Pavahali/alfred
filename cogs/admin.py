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

    @commands.is_owner()
    @commands.command()
    async def update(self, ctx):
        for i in settings.logchannels:
            channel = self.bot.get_channel(i)
            await channel.send("Обновляюсь с гитхаба...")
        logs.log(f'Rebooting', '1')
        os.system("nohup ./scripts/update.sh &")
        exit()


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
