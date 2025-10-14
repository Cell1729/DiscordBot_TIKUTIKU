# コマンド処理
import discord
from discord.ext import commands
from discord import Intents
from reminder import Reminder

GREETINGS_TEXT = "ブンブンハローユーチューブ！どうもJapaneseKoreanUGTVです！こんにちはー！"
GREETINGS_URL = "https://www.twitch.tv/alfrea/clip/TriangularCogentLEDSwiftRage-93khMrEhJ9If7N5g"


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
        server_id = guild.id
        # Botがメッセージ送信可能な最初のテキストチャンネルを取得
        channel = next((c for c in guild.text_channels if c.permissions_for(guild.me).send_messages), None)
        if channel:
            await channel.send(f"{GREETINGS_TEXT}\n{GREETINGS_URL}")