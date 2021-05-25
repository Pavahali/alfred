from discord.ext import commands
import discord
import os

client = commands.Bot(command_prefix='.')
client.remove_command('help')

@client.command()
async def help(ctx):
    await ctx.send('Я ничего не умею!')

@client.command()
async def stats(ctx):
    embed=discord.Embed(title="stats")
    embed.add_field(name="Версия", value="v0.2.1", inline=True)
    embed.add_field(name="Что нового", value=f'+логи', inline=True)
    embed.add_field(name="Размер nohup", value=f"{os.path.getsize('../nohup.out')} байт", inline=True)
    embed.add_field(name="Размер логов", value=f"{os.path.getsize('./logs.log')} байт", inline=True)
    await ctx.send(embed=embed)

client.load_extension(f'cogs.responses')
client.load_extension(f'cogs.events')
client.load_extension(f'cogs.admin')
client.load_extension(f'cogs.errs')

client.run(open('token.txt').read())
