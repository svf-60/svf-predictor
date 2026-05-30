from discord import Object as DiscordObject
from discord.ext import commands

def is_owner(ctx):
    return ctx.author.id == 1146961926480482377

class Admin(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command("shutdown")
    @commands.check(is_owner)
    async def shutdown(self, ctx):
        await ctx.send("shutting down")
        await self.bot.close()
        
    @commands.command("sync")
    @commands.check(is_owner)
    async def sync(self, ctx):
        await self.bot.tree.sync(guild=DiscordObject(1381802014492590080))
        await ctx.send("commands synced")

async def setup(bot):
    await bot.add_cog(Admin(bot))