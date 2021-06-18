from discord.ext import commands


class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def l1ttlemode(self, ctx, action=''):
        if ctx.author.id == 504343489664909322:
            await ctx.send("""```
Traceback (most recent call last):
    File "<stdin>", line 9, in <module>
    File "<stdin>", line 9, in L1ttleO
    File "<stdin>", line 9, in L1ttleO
    File "<stdin>", line 9, in L1ttleO
    [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
```""")
        elif ctx.author.id == 701415574898475108:
            if action == "on":
                self.bot.unload_extension('cogs.events')
                await ctx.send('L1ttleO mode is enabled')
            elif action == "off":
                self.bot.load_extension('cogs.events')
                await ctx.send('L1ttleO mode is disabled')
            else:
                await ctx.send("Avaliable actions: `on`/`off`")
        else:
            await ctx.send("Invalid userid")


def setup(bot):
    bot.add_cog(fun(bot))
