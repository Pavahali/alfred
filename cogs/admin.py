from discord.ext import commands
import discord

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command()
    async def load(self, ctx, cog):
        self.bot.load_extension(f'cogs.{cog}')
        await ctx.send(f'{cog} подгрузился')
        print(f'Включен ког {cog}')

    @commands.is_owner()
    @commands.command()
    async def unload(self, ctx, cog):
        self.bot.unload_extension(f'cogs.{cog}')
        await ctx.send(f'{cog} выключен')
        print(f'Выключен ког {cog}')

    @client.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        channel = self.bot.get_channel(12324234183172)
        await channel.send('Я выключаюсь...')
        await self.bot.logout()


def setup(bot):
    bot.add_cog(MyCog(bot))
