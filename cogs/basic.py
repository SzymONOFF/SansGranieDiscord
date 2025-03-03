from discord.ext import commands

# Moduł podstawowych komend
class Basic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Komenda testowa
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command()
    async def help(self, ctx):
        await ctx.send("Nie ma pomocy.")


async def setup(bot):
    await bot.add_cog(Basic(bot))
