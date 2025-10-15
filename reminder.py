# reminder機能のロジック
from discord.ext import tasks, commands
from datetime import datetime
from models.models import ServerSettings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.utils_csv import get_random_csv_row
import pytz

engine = create_engine('sqlite:///models/db.sqlite3')
Session = sessionmaker(bind=engine)

class Reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_load(self):
        self.reminder_task.start()

    @tasks.loop(seconds=60)
    async def reminder_task(self):
        try:
            jst = pytz.timezone('Asia/Tokyo')
            current_time = datetime.now(jst).strftime("%H:%M")
            session = Session()
            all_settings = session.query(ServerSettings).filter_by(reminder_enabled=1).all()
            for settings in all_settings:
                reminder_time = settings.reminder_time
                channel_id = settings.reminder_channel
                if current_time == reminder_time:
                    channel = self.bot.get_channel(channel_id)
                    if channel:
                        figure, quote, url = get_random_csv_row()
                        await channel.send(f"らいさま今日の格言\n{quote}\n{url}")
            session.close()
        except Exception as e:
            print(f"Error in reminder task: \n{e}")

# Cog登録用setup関数
def setup(bot):
    bot.add_cog(Reminder(bot))
