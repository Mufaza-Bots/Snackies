import settings

bot = settings.getBot(messageContent=True)

@bot.event
async def on_ready():
    print(f"[{bot.user}] has started")
    
    for cmdFile in settings.CMDS_DIR.glob("*.py"):
        if cmdFile.name != "__init__.py":
            await bot.load_extension(f"cmds.{cmdFile.name[:-3]}")

bot.run(settings.BotConfig.token())