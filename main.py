import discord
from commands.command_handler import CommandHandler
from commands.commands import get_commands
from discord import Intents
from discord.ext import tasks
from datetime import datetime
import os
from dotenv import load_dotenv
from lib.utils_csv import get_random_csv_row

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
TEXT_CHANNEL_ID = os.getenv('TEXT_CHANNEL')

intents = Intents.default()
intents.message_content = True

bot = CommandHandler(intents=intents)

# コマンドを一括登録
for cmd in get_commands():
    bot.add_app_command(cmd)

# TEXT_CHANNEL_IDをリスト化
if TEXT_CHANNEL_ID:
    channel_ids = [int(cid.strip()) for cid in TEXT_CHANNEL_ID.split(',')]
else:
    channel_ids = []

@tasks.loop(seconds=60)
async def loop():
    now = datetime.now().strftime('%H:%M')
    if now == '08:50':
        for text_id in channel_ids:
            channel = bot.get_channel(text_id)
            if channel:
                figure, quote, url = get_random_csv_row()
                await channel.send(f"らいさま今日の格言\n{quote}\n{url}")

@bot.event
async def on_ready():
    loop.start()
    print(f'Logged in as {bot.user}')

bot.run(TOKEN)
