# コマンド処理
from discord.ext import commands
from discord import Intents, Interaction
from discord.app_commands import CommandTree
from reminder import Reminder


class CommandHandler(commands.Bot):
    def __init__(self, command_prefix, intents: Intents) -> None:
        super().__init__(command_prefix=command_prefix, intents=intents)
        #self.tree = CommandTree(self)

    def add_app_command(self, command):
        """外部からコマンドを追加するためのメソッド"""
        self.tree.add_command(command)

    async def setup_hook(self):
        await self.add_cog(Reminder(self))
        await self.tree.sync()

    async def on_ready(self):
        await self.tree.sync()
        print(f'Logged in as {self.user}')
