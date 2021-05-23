from discord.ext import commands
import discord


class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_error(self, error):
        error = getattr(error, 'original', error)

        if not isinstance(error, commands.CommandNotFound):
            user = await self.bot.get_user('701415574898475108')
            await user.send(f'Пиздец:\n{error}')

def setup(bot):
    bot.add_cog(events(bot))
