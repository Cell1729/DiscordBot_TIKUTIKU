from discord import app_commands, Interaction
from lib.utils_csv import get_random_csv_row
from lib.utils_json import save_settings, load_settings

@app_commands.command(name="tktk", description="Show a random tikutiku quote")
async def tktk_command(interaction: Interaction):
    """
    csvファイルからランダムに一行選んで返す。
    :param interaction:
    :return:
    """
    figure, quote, url = get_random_csv_row()
    await interaction.response.send_message(f"{quote}\n{url}")

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
        "/tktk_reminder <on|off> : リマインダーのON/OFFを切り替えます。\n"
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
    settings = load_settings()
    settings['reminder_time'] = time
    save_settings(settings)
    await interaction.response.send_message(f"リマインダーは{time}に送信されます")

@app_commands.command(name="tktk_setchannel", description="Set reminder channel")
async def tktk_setchannel_command(interaction: Interaction):
    """
    リマインダーのチャンネルを設定する。
    :param interaction:
    :return:
    """
    settings = load_settings()
    settings['reminder_channel'] = interaction.channel_id
    save_settings(settings)
    await interaction.response.send_message(f"リマインダーは{settings['reminder_time']}にこのチャンネルへ送信されます")

@app_commands.command(name="tktk_reminder", description="Toggle reminder ON/OFF")
async def tktk_reminder_command(interaction: Interaction, onoff: str):
    """
    リマインダーのON/OFFを切り替える。メッセージを送信するところまで実装
    :param interaction:
    :param onoff:
    :return:
    """
    await interaction.response.send_message(f"リマインダー {'enabled' if onoff == 'on' else 'disabled'}")

def get_commands():
    return [
        tktk_command,
        tktk_help_command,
        tktk_settime_command,
        tktk_setchannel_command,
        tktk_reminder_command
    ]
