# コマンド処理
from discord.ext import commands
from discord import Intents, Client, Interaction
from discord.app_commands import CommandTree
from utils import load_settings, save_settings
from dotenv import load_dotenv

class CommandHandler(Client):
    def __init__(self, intents: Intents) -> None:
        super().__init__(intents=intents)
        self.tree = CommandTree(self)

    def add_app_command(self, command):
        """外部からコマンドを追加するためのメソッド"""
        self.tree.add_command(command)

    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        await self.tree.sync()
        print(f'Logged in as {self.user}')
