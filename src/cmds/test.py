import settings
import discord
from discord.ext import commands
from discord import app_commands

bot = settings.getBot(messageContent=True)

"""@commands.command(name="randMsg", hidden=True)
async def getRandomMsg(ctx):
    #channel = bot.get_channel(1230287031926653029)
    messages: list[discord.Message] = [msg async for msg in ctx.channel.history()]
    await ctx.send(messages[1].content) 
    
"""
class testGroup(app_commands.Group):
    @app_commands.command(name="say")
    async def say(self, interaction: discord.Interaction, *, arg: str):
        await interaction.response.send_message(arg)

"""async def setup(bot):
    bot.add_command(say)
    bot.add_command(getRandomMsg)"""