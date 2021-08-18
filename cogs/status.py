from discord.ext import commands, tasks
import discord
import random


class status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.songs = (
            "Brutto - Воины света",
            "Brutto - Родны край",
            "Brutto - Папяроска",
            "Brutto - Матрёшка",

            "Daft Punk - Lose Yourself To Dance",
            "Daft Punk - Giorgio by Moroder",
            "Daft Punk - Instant Crush",
            "Daft Punk - Get Lucky",
            "Daft Punk - Touch",

            "Foo Fighters - Everlong",

            "Led Zeppelin - Stairway to Heaven",
            "Led Zeppelin - Immigrant Song",
            "Led Zeppelin - Tangerine",

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

            "Marcy Playground - Sex & Candy",

            "Marylin Manson - Beautiful People",
            "Marylin Manson - The Fight Song",
            "Marylin Manson - Tainted Love",

            "Pearl Jam - Take The Long Way",
            "Pearl Jam - Do The Evolution",
            "Pearl Jam - Alive",

            "Radiohead - Fake Plastic Trees",
            "Radiohead - High and Dry",
            "Radiohead - Karma Police",
            "Radiohead - No Surprises",
            "Radiohead - Creep",

            "Red Hot Chilli Peppers - Californication",
            "Red Hot Chilli Peppers - Dani California",
            "Red Hot Chilli Peppers - Show (Hey Oh)",
            "Red Hot Chilli Peppers - Can't Stop",
            "Red Hot Chilli Peppers - Otherside",

            "Sex Pistols - God Save The Queen",
            "Sex Pistols - Anarchy in the UK",
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

            "The Cranberries - Hollywood",
            "The Cranberries - Zombie",

            "The Jins - Jack Skellington",
            "The Jins - Death Wish",
            "The Jins - Pop Song",
            "The Jins - She Said",
            "The Jins - Radio",

            "Земфира - Аривидерчи",
            "Земфира - Хочешь?",
            "Земфира - Ромашки",
            "Земфира - Искала",

            "Король и Шут - Танец злобного гения",
            "Король и Шут - Ели мясо мужики",
            "Король и Шут - Дурак и молния",
            "Король и Шут - Лесник"
            "Король и Шут - Ром",

            "Порнофильмы - Прости. Прощай. Привет",
            "Порнофильмы - Я так соскучился",
            "Порнофильмы - Уроки любви",
            "Порнофильмы - Это пройдёт",
            "Порнофильмы - Чужое горе",

            # Jojo endings
            "The Bangles - Walk like an Egyptian",
            "Savage Garden - I want you",
            "Enigma - Modern Crusaders",
            "Yes! - Roundabout",
        )

        self.changer.start()

    @tasks.loop(hours=5.0)
    async def changer(self):
        await self.bot.change_presence(activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=random.choice(self.songs)))

    @changer.before_loop
    async def before_printer(self):
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(status(bot))
