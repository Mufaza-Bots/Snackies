import settings
import discord
from discord import app_commands
from genericpath import exists
from discord.ext import commands
from random import randint

class QuotesGroup(app_commands.Group):
    global dbPath
    dbPath = settings.DATA_DIR / 'quotes.txt'

    @app_commands.command(name="add")
    async def addQuote(self, interaction: discord.Interaction, *, quote: str):
        if not exists(dbPath):
            with open(dbPath, mode='w'):
                pass
        try:
            file = open(dbPath, mode='a')
            file.write(f"{quote}\n")
        finally:
            file.close()

    @app_commands.command(name="quote")
    async def getQuote(self, interaction: discord.Interaction):
        try:
            file = open(dbPath, mode='r')
            quotes = file.readlines()
            rand = randint(0, quotes.__len__()-1)
            await interaction.response.send_message(f"{quotes[rand]}")
        finally:
            file.close()

"""@commands.group(aliases=['q'])
async def quotes(ctx):
    msg: discord.Message = await ctx.channel.fetch_message(ctx.channel.last_message_id)
    await msg.delete()"""
    


#async def setup(bot):
    #bot.add_command(quotes)
    #bot.add_command(getQuote)