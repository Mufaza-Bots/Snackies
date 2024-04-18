import settings
from discord.ext import commands

intents = settings.INTENTS
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@commands.command()
async def test(ctx, *, args):
    await ctx.send(cmds.test.check(args))
bot.add_command(test)