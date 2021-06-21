from discord.ext import commands, tasks
import discord
import random


class status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.songs = [
            "Metallica - Nothing Else Matters",
            "Metallica - The Unforgiven",
            "Metallica - Enter Sandman",
            "Metallica - Sad But True",

            "Nirvana - Smells Like Teen Spirit",
            "Nirvana - Heart-Shaped Box",
            "Nirvana - Rape Me",
            "Nirvana - Polly",
            "Nirvana - Dumb",

            "Nizkiz - Небяспечна",
            "Nizkiz - Интроверт",
            "Nizkiz - Полночь",
            "Nizkiz - Правiлы",
            "Nizkiz - Блiзка",

            "Radiohead - Fake Plastic Trees",
            "Radiohead - High and Dry",
            "Radiohead - Karma Police",
            "Radiohead - No Surprises",
            "Radiohead - Creep",

            "Sex Pistols - God Save The Queen",
            "Sex Pistols - Anarchy In The UK",
            "Sex Pistols - I Wanna Be Me",
            "Sex Pistols - Bodies",

            "System Of A Down - Lost In Hollywood",
            "System Of A Down - Chop Suey!",
            "System Of A Down - Lonely Day",
            "System Of A Down - Toxicity",
            "System Of A Down - Aerials",

            "The Beatles - Here Comes The Sun",
            "The Beatles - Yellow Submarine"
            "The Beatles - Come Together",
            "The Beatles - Let It Be",
            "The Beatles - Yesterday",

            "Порнофильмы - Россия для грусных",
            "Порнофильмы - Уроки любви",
            "Порнофильмы - Это пройдёт",
            "Порнофильмы - Чужое горе",
            ]

        self.changer.start()

    @tasks.loop(minutes=5.0)
    async def changer(self):
        await self.bot.change_presence(activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=random.choice(self.songs)))

    @changer.before_loop
    async def before_printer(self):
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(status(bot))