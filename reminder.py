# reminder機能のロジック
from discord.ext import tasks, commands
from datetime import datetime
from lib.utils_json import load_settings
from lib.utils_csv import get_random_csv_row

class Reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_load(self):
        self.reminder_task.start()

    @tasks.loop(seconds=60)
    async def reminder_task(self):
        current_time = datetime.now().strftime("%H:%M")
        all_settings = load_settings()
        for guild_id, settings in all_settings.items():
            if not settings.get("reminder_enabled"):
                continue
            reminder_time = settings.get("reminder_time")
            channel_id = settings.get("reminder_channel")
            if reminder_time and channel_id and current_time == reminder_time:
                channel = self.bot.get_channel(channel_id)
                if channel:
                    figure, quote, url = get_random_csv_row()
                    await channel.send(f"らいさま今日の格言\n{quote}\n{url}")

# Cog登録用setup関数
def setup(bot):
    bot.add_cog(Reminder(bot))
