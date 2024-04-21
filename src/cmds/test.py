import discord
from discord.ext import commands

@commands.command()
async def say(ctx, arg: str):
    await ctx.send(arg)

async def setup(bot):
    bot.add_command(say)