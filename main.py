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
    embed.add_field(name="Версия", value="v0.1.4", inline=True)
    embed.add_field(name="Размер nohup", value=f"{os.path.getsize('./nohup.out')} байт", inline=True)
    await ctx.send(embed=embed)

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
