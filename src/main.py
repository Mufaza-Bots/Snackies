import settings
import discord
from discord.ext import commands, tasks


intents = discord.Intents.default()
intents.message_content = True

build = settings.API

bot = commands.Bot(command_prefix=build.PREFIX, intents=intents)

async def is_moderator(ctx):
    for userRole in ctx.author.roles:
        for serverRole in settings.MODERATOR_ROLE_ID_LIST:
            if userRole.id == serverRole:
                return True
    return False

@tasks.loop(hours=2)
async def cleanup():
    channel = bot.get_channel(settings.CHANNEL_ID)
    messages = [None]
    async for msg in channel.history():
        if discord.utils.utcnow().day - msg.created_at.day > 0 or discord.utils.utcnow().day - msg.created_at.day < 0:
            messages += [msg]
    await channel.delete_messages(messages=messages[1:])
    print(f"Cleanup ran [{discord.utils.utcnow()}]")

@bot.event
async def on_ready():
    print(f"[{bot.user}] has started")
"""
@bot.command(name="age")
async def getAge(ctx, msgID: int):
    message: discord.Message = await ctx.fetch_message(msgID)
    
    
    await ctx.send(f"Age of the message is: {discord.utils.utcnow().day}")
"""    
    
@bot.command(name="mc")
#@commands.check(is_moderator)
async def manualclean(ctx):
    channel = bot.get_channel(ctx.channel.id)
    messages = [None]
    async for msg in channel.history():
        if discord.utils.utcnow().minute - msg.created_at.minute > 1 or discord.utils.utcnow().minute - msg.created_at.minute < -1:
            messages += [msg]
    await channel.delete_messages(messages=messages[1:])
"""
@bot.command()
async def time(ctx):
    boolcheck = False
    for role in ctx.author.roles:
        if role.id == 890583013497380946:
            boolcheck = True
    
    await ctx.send(boolcheck)"""

@bot.command()
#@commands.check(is_moderator)
async def clean(ctx, arg: str):
    cleanCH = bot.get_channel(settings.CHANNEL_ID)
    arg = arg.lower()
    if arg == "start":
        cleanup.start()
        print(f"starting cleanup in #{cleanCH.name}")
    elif arg == "stop":
        cleanup.stop()
        print(f"Stopping cleanup in #{cleanCH.name}")
    else:
        await ctx.send(f"Use either start or stop")
        
    
bot.run(build.DISCORD_TOKEN)  #change me