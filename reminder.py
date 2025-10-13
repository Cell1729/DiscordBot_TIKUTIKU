# reminder機能のロジック
from discord.ext import tasks, commands
from lib.utils_json import load_settings

class Reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reminder_task.start()

    @tasks.loop(minutes=1)
    async def reminder_task(self):
        settings = load_settings()
        if settings['reminder_enabled']:
            # 時間が一致したらメッセージ送信
            # ...送信処理...

def setup(bot):
    bot.add_cog(Reminder(bot))
