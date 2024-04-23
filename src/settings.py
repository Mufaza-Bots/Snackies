import pathlib
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = pathlib.Path(__file__).parent
CMDS_DIR = BASE_DIR / "cmds"
DATA_DIR = BASE_DIR / "data"

CHANNEL_ID = 1230297486342488094
MODERATOR_ROLE_ID_LIST = [
    836554939018903552, #Duchess
    836160114222301184, #Admin
    836160051626377267  #Moderator
]
"""
class API:
    DISCORD_TOKEN = os.getenv("DISCORD_API_TOKEN")
    PREFIX = "!"

class DEV:
    DISCORD_TOKEN = os.getenv("DEV_TOKEN")
    PREFIX = "."
"""
class BotConfig():
    global dev
    dev = False
    
    def prefix():
        if dev:
            return "."
        return "!"
    def token():
        if dev:
            return os.getenv("DEV_TOKEN")
        return os.getenv("DISCORD_API_TOKEN")
    def intents():
        return discord.Intents.default()

def getBot(prefix=BotConfig.prefix(), intents=BotConfig.intents(), messageContent=False):
    intents.message_content = messageContent
    bot = commands.Bot(command_prefix=prefix, intents=intents)
    return bot