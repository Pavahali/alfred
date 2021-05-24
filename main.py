from discord.ext import commands
import discord

client = commands.Bot(command_prefix='.')
client.remove_command('help')

@client.command()
async def help(ctx):
    await ctx.send('Я ничего не умею!')

@client.command()
async def version(ctx):
    await ctx.send('0.1.3')

client.load_extension(f'cogs.errs')
client.load_extension(f'cogs.events')
client.load_extension(f'cogs.admin')

client.run(open('token.txt').read())
