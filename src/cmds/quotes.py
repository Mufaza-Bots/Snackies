import settings
import discord
from genericpath import exists
from discord.ext import commands
from random import randint

@commands.group(aliases=['q'])
async def quotes(ctx):
    msg: discord.Message = await ctx.channel.fetch_message(ctx.channel.last_message_id)
    await msg.delete()
    
dbPath = settings.DATA_DIR / 'quotes.txt'

@quotes.command(name="add")
async def addQuote(ctx, *, quote):
    if not exists(dbPath):
        with open(dbPath, mode='w'):
            pass
    try:
        file = open(dbPath, mode='a')
        file.write(f"{quote}\n")
    finally:
        file.close()

@quotes.command(name="quote")
async def getQuote(ctx):
    try:
        file = open(dbPath, mode='r')
        quotes = file.readlines()
        rand = randint(0, quotes.__len__()-1)
        await ctx.send(f"{quotes[rand]}")
    finally:
        file.close()

async def setup(bot):
    bot.add_command(quotes)
    bot.add_command(getQuote)