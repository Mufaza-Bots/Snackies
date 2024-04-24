import settings
from cmds import test, quotes

bot = settings.getBot(messageContent=True)

async def syncTree(bot):
    guild = bot.get_guild(851491243829362768)
    bot.tree.copy_global_to(guild=guild)
    await bot.tree.sync(guild=guild)

@bot.event
async def on_ready():
    print(f"[{bot.user}] has started")
    
    """for cmdFile in settings.CMDS_DIR.glob("*.py"):
        if cmdFile.name != "__init__.py":
            await bot.load_extension(f"cmds.{cmdFile.name[:-3]}")"""
    #await syncTree(bot=bot)
    
    tests = test.testGroup(name="testcmd", description="desc ription")
    bot.tree.add_command(tests)
    
    quote = quotes.QuotesGroup(name="quotes")
    bot.tree.add_command(quote)


bot.run(settings.BotConfig.token())