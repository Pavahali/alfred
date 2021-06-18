from discord.ext import commands, tasks
from cogs import db
import discord
import random


class status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.songs = [
            "Nirvana - Rape Me",
            "Nirvana - Polly",
            "Nirvana - Dumb",
            "Nirvana - Heart-Shaped Box",
            "Nirvana - Smells Like Teen Spirit",

            "Radiohead - Karma Police",
            "Radiohead - No Surprises",
            "Radiohead - Creep",

            "Nizkiz - Небяспечна",
            "Nizkiz - Правiлы",
            "Nizkiz - Блiзка",

            "Порнофильмы - Это пройдёт",
            "Порнофильмы - Россия для грусных",
            "Порнофильмы - Уроки любви",
            "Порнофильмы - Чужое горе"
            ]

        self.changer.start()

    @tasks.loop(minutes=3.0)
    async def changer(self):
        await self.bot.change_presence(activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=random.choice(self.songs)))

    @changer.before_loop
    async def before_printer(self):
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(status(bot))
