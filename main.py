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
    embed.add_field(name="Версия", value="v0.1.6", inline=True)
    embed.add_field(name="Размер nohup", value=f"{os.path.getsize('./nohup.out')} байт", inline=True)
    await ctx.send(embed=embed)

client.load_extension(f'cogs.errs')
client.load_extension(f'cogs.events')


client.run(open('token.txt').read())
