from discord.ext import commands
import discord


class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Я запустився')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.mentions:
            pings = []
            for i in message.mentions:
                pings.append(str(i))
            if str(message.author) in pings:
                await message.channel.send('Селфпинг? :face_with_raised_eyebrow:')

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
                msg = f'Удалено сообщение {message.author} с пингами:```'
                for i in pings:
                    msg += i + '\n'
                await message.channel.send(msg + '```')
            await message.channel.send(f"Содержание:```{message.content}```")

            if 'Aibat#1262' in pings:
                await message.channel.send(f"Айбат, не шали :smirk:")

def setup(bot):
    bot.add_cog(events(bot))
