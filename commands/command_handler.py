# コマンド処理
import discord
from discord.ext import commands
from discord import Intents
from reminder import Reminder
from models.models import ServerSettings
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

GREETINGS_TEXT = "ブンブンハローユーチューブ！どうもJapaneseKoreanUGTVです！こんにちはー！"
GREETINGS_URL = "https://www.twitch.tv/alfrea/clip/TriangularCogentLEDSwiftRage-93khMrEhJ9If7N5g"

engine = create_engine('sqlite:///models/db.sqlite3')
Session = sessionmaker(bind=engine)
session = Session()

class CommandHandler(commands.Bot):
    def __init__(self, command_prefix, intents: Intents) -> None:
        super().__init__(command_prefix=command_prefix, intents=intents)

    def add_app_command(self, command):
        """外部からコマンドを追加するためのメソッド"""
        self.tree.add_command(command)

    async def setup_hook(self):
        await self.add_cog(Reminder(self))
        await self.tree.sync()

    async def on_ready(self):
        await self.tree.sync()
        print(f'Logged in as {self.user}')

    async def on_guild_join(self, guild: discord.Guild):
        """
        サーバーに参加したときに呼ばれるイベントハンドラ。
        :param guild:
        :return:
        """
        server_id = str(guild.id)
        channel = next((c for c in guild.text_channels if c.permissions_for(guild.me).send_messages), None)
        reminder_channel_id = channel.id if channel else None
        reminder_channel_name = channel.name if channel else "未設定"
        exists = session.query(ServerSettings).filter_by(server_id=server_id).first()
        if not exists:
            new_setting = ServerSettings(
                server_id=server_id,
                reminder_time="8:50",
                reminder_channel=reminder_channel_id,
                reminder_channel_name=reminder_channel_name,
                reminder_enabled=0
            )
            session.add(new_setting)
            session.commit()
        session.close()
        if channel:
            await channel.send(f"{GREETINGS_TEXT}\n{GREETINGS_URL}")