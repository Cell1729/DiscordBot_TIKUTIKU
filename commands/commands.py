from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.quotes_extract import RandomQuoteExtractor
from lib.utils_json import save_guild_settings, load_guild_settings
from discord import app_commands, Interaction
import os

db_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'db.sqlite3')
engine = create_engine(f'sqlite:///{os.path.abspath(db_path)}')
SESSION = sessionmaker(bind=engine)


@app_commands.command(name="tktk", description="Show a random tikutiku quote")
async def tktk_command(interaction: Interaction):
    """
    データベースからランダムに一行選んで返す。
    :param interaction:
    :return:
    """
    session = SESSION()
    extractor = RandomQuoteExtractor(session)
    quote, url = extractor.get_random_quote()
    session.close()
    if quote:
        await interaction.response.send_message(f"{quote}\n{url}")
    else:
        await interaction.response.send_message("データベースに名言が登録されていません。")

@app_commands.command(name="tktk_help", description="Show help for tikutiku bot")
async def tktk_help_command(interaction: Interaction):
    """
    ヘルプメッセージを返す。
    :param interaction:
    :return:
    """
    help_text = (
        "/tktk : ランダムに1つちくちく言葉を返します。\n"
        "/tktk_help : helpの表示します。\n"
        "/tktk_settime <HH:MM> : リマインダー時間を設定します。\n"
        "/tktk_setchannel : リマインダーのチャンネルを設定します。\n"
        "/tktk_reminder <on|off> : リマインダーのon/offを切り替えます。\n"
    )
    await interaction.response.send_message(help_text)

@app_commands.command(name="tktk_settime", description="Set reminder time (HH:MM)")
async def tktk_settime_command(interaction: Interaction, time: str):
    """
    リマインダーの時間を設定する。
    :param interaction:
    :param time:
    :return:
    """
    guild_id = interaction.guild_id
    settings = load_guild_settings(guild_id)
    settings['reminder_time'] = time
    save_guild_settings(guild_id, settings)
    channel_name = interaction.channel.name if interaction.channel else "未設定"
    await interaction.response.send_message(f"リマインダーは{time}に「{channel_name}」へ送信されます")

@app_commands.command(name="tktk_setchannel", description="Set reminder channel")
async def tktk_setchannel_command(interaction: Interaction):
    """
    リマインダーのチャンネルを設定する。
    :param interaction:
    :return:
    """
    guild_id = interaction.guild_id
    settings = load_guild_settings(guild_id)
    settings['reminder_channel'] = interaction.channel_id
    save_guild_settings(guild_id, settings)
    await interaction.response.send_message(f"リマインダーは{settings['reminder_time']}に「{interaction.channel.name}」へ送信されます")

@app_commands.command(name="tktk_reminder", description="Toggle reminder ON/OFF")
async def tktk_reminder_command(interaction: Interaction, onoff: str):
    """
    リマインダーのON/OFFを切り替える。メッセージを送信するところまで実装
    :param interaction:
    :param onoff:
    :return:
    """
    guild_id = interaction.guild_id
    settings = load_guild_settings(guild_id)
    settings['reminder_enabled'] = (onoff == 'on')
    save_guild_settings(guild_id, settings)
    await interaction.response.send_message(f"リマインダー {'enabled' if onoff == 'on' else 'disabled'}")

def get_commands():
    return [
        tktk_command,
        tktk_help_command,
        tktk_settime_command,
        tktk_setchannel_command,
        tktk_reminder_command
    ]
