from discord.ext import commands
import discord

client = commands.Bot(command_prefix='$')
client.remove_command('help')

@client.command()
async def help(ctx):
    await ctx.send('Я ничего не умею!')

@client.event
async def on_ready():
    print('Я запустився')

@client.event
async def on_message_delete(message):
    if message.mentions:

        pings = []
        for i in message.mentions:
            pings.append(str(i))

        if len(pings) == 1:
            if not str(message.author) in pings:
                await message.channel.send(f'Удалено сообщение {message.author} с пингом {pings[0]}')
        else:
            msg = f'Удалено сообщение {message.author} с пингами:```'
            for i in pings:
                msg += i + '\n'
            await message.channel.send(msg+'```')


client.run(open('token.txt').read())
