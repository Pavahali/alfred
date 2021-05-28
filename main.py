from discord.ext import commands
import setproctitle as pt
import discord
import os

pt.setproctitle('alfred')

intents = discord.Intents().all()
client = commands.Bot(command_prefix='.', intents=intents)
client.remove_command('help')


@client.command()
async def help(ctx):
    await ctx.send('Я ничего не умею!')

@client.command()
async def stats(ctx):
    embed=discord.Embed(title="stats")
    embed.add_field(name="Версия", value="v0.4", inline=True)
    embed.add_field(name="Название процесса", value=pt.getproctitle(), inline=True)
    embed.add_field(name="Размер nohup", value=f"{round(os.path.getsize('nohup.out') / 1024, 2)} килобайт", inline=False)
    embed.add_field(name="Размер логов", value=f"{round(os.path.getsize('logs.log') / 1024, 2)} килобайт", inline=True)
    embed.add_field(name="Размер бд", value=f"{round(os.path.getsize('cogs/db.json') / 1024, 2)} килобайт", inline=True)
    await ctx.send(embed=embed)

client.load_extension('cogs.responses')
client.load_extension('cogs.events')
client.load_extension('cogs.admin')
client.load_extension('cogs.comms')
client.load_extension('cogs.errs')

client.run(open('token.txt').read())
