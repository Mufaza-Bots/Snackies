import datetime
from logging import Logger
import settings
import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

async def is_moderator(ctx):
    for userRole in ctx.author.roles:
        for serverRole in settings.MODERATOR_ROLE_ID_LIST:
            if userRole.id == serverRole:
                return True
    return False

@tasks.loop(hours=24)
async def cleanup():
    channel = bot.get_channel(settings.CHANNEL_ID)
    messages = [msg async for msg in channel.history()]
    await channel.delete_messages(messages=messages)
    print("Cleanup ran")

@bot.event
async def on_ready():
    print(f"[{bot.user}] has started")
    
    
@bot.command()
@commands.check(is_moderator)
async def manualclean(ctx, channel: discord.TextChannel):
    channel = bot.get_channel(channel.id)
    messages = [msg async for msg in channel.history()]
    await channel.delete_messages(messages=messages)
"""
@bot.command()
async def time(ctx):
    boolcheck = False
    for role in ctx.author.roles:
        if role.id == 890583013497380946:
            boolcheck = True
    
    await ctx.send(boolcheck)"""

@bot.command()
@commands.check(is_moderator)
async def clean(ctx, arg: str):
    arg = arg.lower()
    if arg == "start":
        cleanup.start()
        print(f"starting cleanup")
    elif arg == "stop":
        cleanup.stop()
        print(f"Stopping cleanup")
    else:
        await ctx.send(f"Use either start or stop")
        
    
bot.run(settings.DISCORD_API_SECRET)