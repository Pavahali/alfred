from discord.ext import commands
from exts import logs
import aiosqlite
import settings
import gc


class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Я запустився')
        for i in settings.logchannels:
            channel = self.bot.get_channel(i)
            await channel.send("Я Лунтик! Я снова с вами!")
        gc.enable()
        logs.log('bot has started', '0')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.mentions:
            for mentioned in message.mentions:
                if mentioned != message.author:
                    user = []
                    async with aiosqlite.connect(settings.db) as db:
                        async with db.execute("SELECT lastpings FROM users WHERE id = ?", (mentioned.id,)) as cursor:
                            async for row in cursor:
                                user = row[0].split(';')
                            if not user:
                                await db.execute("INSERT INTO users(id, lastpings) VALUES(?, ?)", (mentioned.id, '',))

                        if len(user) >= settings.pinglimit:
                            user.pop(0)
                        user.append(str(message.author.id))
                        user = ';'.join(user)

                        await db.execute("UPDATE users SET lastpings=? WHERE id=?", (user, mentioned.id,))
                        await db.commit()

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
                    await message.channel.send('Удалено сообщение, с пингом меня')
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
            if message.content.startswith("Удалено сообщение"):
                await message.channel.send(f'Кто-то удалил сообщение... Я написал, что:\n{message.content}')
            elif message.content.startswith("Кто-то удалил"):
                await message.channel.send(f'Кто-то удалил сообщение... Я написал, что:\n{message.content[43:]}')


def setup(bot):
    bot.add_cog(events(bot))
