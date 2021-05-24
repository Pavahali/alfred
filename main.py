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

@commands.is_owner()
@client.command()
async def load(ctx, cog):
    client.load_extension(f'cogs.{cog}')
    await ctx.send(f'{cog} подгрузился')
    print(f'Включен ког {cog}')

@commands.is_owner()
@client.command()
async def unload(ctx, cog):
    client.unload_extension(f'cogs.{cog}')
    await ctx.send(f'{cog} выключен')
    print(f'Выключен ког {cog}')

client.load_extension(f'cogs.errs')
client.load_extension(f'cogs.events')


client.run(open('token.txt').read())
