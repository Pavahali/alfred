from discord.ext import commands
import settings
import discord


intents = discord.Intents().all()
client = commands.Bot(command_prefix='.', intents=intents,
                      case_insensitive=True)
client.remove_command('help')


@client.group()
async def help(ctx):
    if not ctx.invoked_subcommand:
        embed = discord.Embed(title="Категории")
        embed.add_field(
            name="users", value="`whopinged`, `userinfo`", inline=True)
        embed.add_field(
            name="setup", value="<Тут пока ничего нет>", inline=True)
        embed.add_field(
            name="other", value="`ascii`, `clear`, `echo`", inline=True)
        await ctx.send(embed=embed)


@help.command()
async def users(ctx):
    embed = discord.Embed(
        title="Users", description="Команды связанные с юзерами")
    embed.add_field(
        name="whopigned", value="Просмотр последних пингов. Алиас: `ктопнул`", inline=False)
    embed.add_field(name="userinfo",
                    value="Просмотр информации о юзвере", inline=False)
    await ctx.send(embed=embed)


@help.command()
async def setup(ctx):
    embed = discord.Embed(title="Setup", descriptiom="Настройка бота")
    await ctx.send(embed=embed)


@help.command()
async def other(ctx):
    embed = discord.Embed(
        title="Other", description="Команды не попадающие не под какую категорию")
    embed.add_field(
        name="ascii", value="Вывод сообщения ascii артом", inline=False)
    embed.add_field(name="echo", value="Повтор сообщения", inline=False)
    embed.add_field(name="clear", value="Очистка чата", inline=False)
    await ctx.send(embed=embed)


@help.command()
async def whopinged(ctx):
    embed = discord.Embed(title="whopinged")
    embed.add_field(name="Использование", value="`.whopinged`", inline=True)
    embed.add_field(name="Описание",
                    value="Просмотр последних пингов", inline=True)
    embed.add_field(name="Алиасы", value="`ктопнул`", inline=True)
    await ctx.send(embed=embed)


@help.command()
async def userinfo(ctx):
    embed = discord.Embed(title="userinfo")
    embed.add_field(name="Использование",
                    value="`.userinfo <пинг>`,`.userinfo <айди>`", inline=False)
    embed.add_field(name="Описание",
                    value="Просмотр информации о юзвере", inline=False)
    await ctx.send(embed=embed)


@help.command()
async def ascii(ctx):
    embed = discord.Embed(title="ascii")
    embed.add_field(name="Использование",
                    value="`.ascii <сообщение>`", inline=False)
    embed.add_field(name="Описание",
                    value="Вывод сообщения ascii артом", inline=False)
    await ctx.send(embed=embed)


@help.command()
async def clear(ctx):
    embed = discord.Embed(title="ascii")
    embed.add_field(name="Использование",
                    value="`.clear <кол-во сообщений>`", inline=False)
    embed.add_field(name="Описание", value="Очистка чата", inline=False)
    await ctx.send(embed=embed)


@help.command()
async def echo(ctx):
    embed = discord.Embed(title="echo")
    embed.add_field(name="Использование",
                    value="`.echo <сообщение>`", inline=False)
    embed.add_field(name="Описание", value="Повтор сообщения", inline=False)
    embed.add_field(name="Алиасы", value="`moodyblues`,`repeat`", inline=False)
    await ctx.send(embed=embed)

for cog in settings.cogs:
    client.load_extension(cog)

client.run(settings.token)
