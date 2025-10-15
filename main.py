import discord
from commands.command_handler import CommandHandler
from commands.commands import get_commands
from discord import Intents
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
TEXT_CHANNEL_ID = os.getenv('TEXT_CHANNEL')

intents = Intents.default()
intents.message_content = True

bot = CommandHandler(command_prefix="!", intents=intents)

# コマンドを一括登録
for cmd in get_commands():
    bot.add_app_command(cmd)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

bot.run(TOKEN)
