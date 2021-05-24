from discord.ext import commands
import discord

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command()
    async def load(self, ctx, cog):
        client.load_extension(f'cogs.{cog}')
        await ctx.send(f'{cog} подгрузился')
        print(f'Включен ког {cog}')

    @commands.is_owner()
    @commands.command()
    async def unload(self, ctx, cog):
        client.unload_extension(f'cogs.{cog}')
        await ctx.send(f'{cog} выключен')
        print(f'Выключен ког {cog}')




def setup(bot):
    bot.add_cog(MyCog(bot))
