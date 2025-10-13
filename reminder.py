# reminder機能のロジック
from discord.ext import tasks, commands
from datetime import datetime
from lib.utils_json import load_settings
from lib.utils_csv import get_random_csv_row
import os

SEND_TIME = "08:50"

class Reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_load(self):
        self.reminder_task.start()

    @tasks.loop(seconds=60)
    async def reminder_task(self):
        current_time = datetime.now().strftime("%H:%M")
        TEXT_CHANNEL_ID = os.getenv('TEXT_CHANNEL')
        # 環境変数からデータを配列化
        if TEXT_CHANNEL_ID:
            channel_ids = [int(cid.strip()) for cid in TEXT_CHANNEL_ID.split(',')]
        else:
            channel_ids = []

        # 定刻になったらメッセージを送信
        if current_time == SEND_TIME:
            for text_id in channel_ids:
                channel = self.bot.get_channel(text_id)
                if channel:
                    result = get_random_csv_row()
                    if result and len(result) >= 3:
                        figure, quote, url = result
                        await channel.send(f"らいさま今日の格言\n{quote}\n{url}")

# Cog登録用setup関数
def setup(bot):
    bot.add_cog(Reminder(bot))
