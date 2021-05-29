from discord.ext import commands
from cogs import logs
import discord

class responses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(responses(bot))
