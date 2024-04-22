import settings
import discord
from discord.ext import commands

bot = settings.getBot()

@commands.command(hidden=True)
async def say(ctx):
    await ctx.send(ctx.channel.name)

@commands.command(name="randMsg", hidden=True)
async def getRandomMsg(ctx):
    #channel = bot.get_channel(1230287031926653029)
    messages: list[discord.Message] = [msg async for msg in ctx.channel.history()]
    await ctx.send(messages[1].content)

async def setup(bot):
    bot.add_command(say)
    bot.add_command(getRandomMsg)
