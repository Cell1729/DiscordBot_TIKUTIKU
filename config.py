import os

# 設定(トークン、リマインダー等)

BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN', 'YOUR_DISCORD_BOT_TOKEN')

# リマインダーのデフォルト時刻
DEFAULT_REMINDER_TIME = '08:00'

# リマインダーのデフォルトチャンネルID（未設定ならNone）
DEFAULT_REMINDER_CHANNEL = None
