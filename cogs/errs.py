from discord.ext import commands
import discord
import logs

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_error(self, error):
        error = getattr(error, 'original', error)

        if not isinstance(error, commands.CommandNotFound):
            user = client.get_user(381870129706958858)
            await user.send(error)
            logs.log(error,'2')

def setup(bot):
    bot.add_cog(events(bot))
