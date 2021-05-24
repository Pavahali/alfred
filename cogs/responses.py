from discord.ext import commands
import discord


class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #reactions
    @commands.Cog.listener()
    async def on_message(self, message):
        responces = [
        [["споки", "сн", "спокойной ночи"], "🌑"],
        [["утречка", "доброе утро"], "🌞"],
        [["ку", "прив", "привет", "хай"], "👋"]
        ]
        
        for j in responces:
            for i in j[0]:
                if i in message.content:
                    await message.add_reaction(j[1])

def setup(bot):
    bot.add_cog(events(bot))
