from discord.ext import commands
import datetime as dt
from cogs import logs
from cogs import db
import discord

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Я запустився')
        channel = self.bot.get_channel(618044439939645444)
        await channel.send("Я Лунтик! Я снова с вами!")
        logs.log('bot has started', '0')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.mentions:
            for i in message.mentions:
                user = await db.ruser(i.id)
                user["lastpinged"].append({"id":str(message.author.id), "time": dt.timestamp()})
                user["lastpinged"].pop(0)
                await db.wuser(i.id, user)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.mentions:
            pings = []
            for i in message.mentions:
                pings.append(str(i))

            if len(pings) == 1:
                if str(message.author) in pings:
                    return
                elif 'alfred#0683' in pings:
                    await message.channel.send(f'Удалено сообщение, с пингом меня')
                    return
                await message.channel.send(f'Удалено сообщение `{message.author}` с пингом `{pings[0]}`\n')
            else:
                msg = f'Удалено сообщение `{message.author}` с пингами:\n```'
                for i in pings:
                    msg += i + '\n'
                await message.channel.send(msg + '\n```\n')
            await message.channel.send(f"Содержание:\n```\n{message.content}\n```")

        if str(message.author) == 'alfred#0683':
            logs.log('somebody deleted my message', '0')
            if message.content.startswith("Удалено"):
                await message.channel.send(f'Кто-то удалил сообщение... Я написал, что:\n{message.content}')
            elif message.content.startswith('Кто-то удалил'):
                await message.channel.send(f'Кто-то удалил сообщение... Я написал, что:\n{message.content[43:]}')


def setup(bot):
    bot.add_cog(events(bot))
