import pathlib
import os
import discord
from dotenv import load_dotenv


load_dotenv()
DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")

BASE_DIR = pathlib.Path(__file__).parent
CMDS_DIR = BASE_DIR / "cmds"

INTENTS = discord.Intents.all()

CHANNEL_ID = 1230297486342488094
MODERATOR_ROLE_ID_LIST = [
    836554939018903552, #Duchess
    836160114222301184, #Admin
    836160051626377267  #Moderator
]