from discord.ext import commands
import discord


class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Я запустився')
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="v0.1.6"))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.mentions:
            pings = []
            for i in message.mentions:
                pings.append(str(i))

            if str(message.author) in pings:
                await message.channel.send('Селфпинг? :face_with_raised_eyebrow:')
            if 'alfred#0683' in pings:
                await message.channel.send('Ахуел?')

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.mentions:

            pings = []
            for i in message.mentions:
                pings.append(str(i))

            if len(pings) == 1:
                if str(message.author) in pings:
                    return
                await message.channel.send(f'Удалено сообщение {message.author} с пингом {pings[0]}')
            else:
                msg = f'Удалено сообщение {message.author} с пингами:\n```'
                for i in pings:
                    msg += i + '\n'
                await message.channel.send(msg + '\n```')
            await message.channel.send(f"Содержание:\n```\n{message.content}\n```")

            if str(message.author) == 'Aibat#1262':
                await message.channel.send(f"Айбат, не шали :smirk:")
        if str(message.author) == 'alfred#0683':
            await message.channel.send(f"Умный дохуя удалять моё сообщение?")
            if message.content.startswith("Удалено"):
                await message.channel.send(f'Я написал, что:\n{message.content}')

def setup(bot):
    bot.add_cog(events(bot))
