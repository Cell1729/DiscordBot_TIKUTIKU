# reminder機能のロジック
from discord.ext import tasks, commands
from datetime import datetime
from lib.utils_json import load_settings
from lib.utils_csv import get_random_csv_row

class Reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reminder_task.start()

    @tasks.loop(minutes=1)
    async def reminder_task(self):
        settings = load_settings()
        current_time = datetime.now().strftime("%H:%M")
        # テスト用: 無条件でONにしたい場合はif True: に変更可能
        # settings.get('reminder_enabled') and
        if current_time == "17:56":
            channel_id = settings.get('reminder_channel')
            channel = self.bot.get_channel(channel_id) if channel_id else None
            if channel:
                result = get_random_csv_row()
                if result and len(result) >= 3:
                    figure, quote, url = result
                    await channel.send(f"今日のらいさま\n{quote}\n{url}")
                else:
                    await channel.send("今日はチクチクなし!")

# Cog登録用setup関数
def setup(bot):
    bot.add_cog(Reminder(bot))
