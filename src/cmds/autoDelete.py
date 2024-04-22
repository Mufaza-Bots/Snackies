import settings
import discord
from discord.ext import commands, tasks

bot = settings.getBot(messageContent=True)
autoChannel: discord.TextChannel = None
autoRunning = False

async def is_moderator(ctx):
    for userRole in ctx.author.roles:
        for serverRole in settings.MODERATOR_ROLE_ID_LIST:
            if userRole.id == serverRole:
                return True
    return False

async def cleanup():
    currentTime = discord.utils.utcnow()
    messages = []
    async for msg in autoChannel.history():
        if (currentTime.date().toordinal() - msg.created_at.date().toordinal()) > 0:
            messages.append(msg)
    if messages.__len__() > 0:
        await autoChannel.delete_messages(messages=messages)
        print(f"Cleanup ran [{currentTime}]")

async def runCheck(running: bool):
    global autoRunning
    autoRunning = running

@commands.group()
async def clean(ctx):
    msg: discord.Message = await ctx.channel.fetch_message(ctx.channel.last_message_id)
    await msg.delete()

@clean.command(name="start")
#@commands.check(is_moderator)
async def startAutoClean(ctx):
    global autoChannel
    if autoRunning:
        await ctx.send(f"AutoCleaner is running in #{autoChannel.name}")
        return
    autoCleaner.start()
    print(f"starting cleanup in #{ctx.channel.name}")
    await runCheck(True)
    autoChannel = ctx.channel

@clean.command(name="stop")
#@commands.check(is_moderator)
async def stopAutoClean(ctx):
    autoCleaner.stop()
    print(f"Stopping cleanup in #{ctx.channel.name}")
    await runCheck(False)

@tasks.loop(hours=2)
async def autoCleaner():
    await cleanup()

@commands.command(name="mc")
#@commands.check(is_moderator)
async def manualclean(ctx):
    messages = [None]
    async for msg in ctx.channel.history():
        if discord.utils.utcnow().minute - msg.created_at.minute > 1 or discord.utils.utcnow().minute - msg.created_at.minute < -1:
            messages += [msg]
    await ctx.channel.delete_messages(messages=messages[1:])


async def setup(bot):
    bot.add_command(clean)
    bot.add_command(manualclean)