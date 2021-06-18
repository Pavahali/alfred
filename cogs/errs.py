from discord.ext import commands
from cogs import logs
import discord


class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_error(self, error):
        error = getattr(error, 'original', error)

        if not isinstance(error, commands.CommandNotFound):
            user = self.bot.fetch_user(701415574898475108)
            await user.send(error)
            logs.log(error, '2')


def setup(bot):
    bot.add_cog(events(bot))
