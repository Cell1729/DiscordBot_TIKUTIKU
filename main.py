import discord
from commands.command_handler import CommandHandler
from commands.commands import get_commands
from discord import Intents
from reminder import Reminder
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True

bot = CommandHandler(intents=intents)

# コマンドを一括登録
for cmd in get_commands():
    bot.add_app_command(cmd)

# リマインダー機能を追加
bot.add_cog(Reminder(bot))
bot.run(TOKEN)
