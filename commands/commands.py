from discord import app_commands, Interaction

@app_commands.command(name="tktk", description="Show a random tikutiku quote")
async def tktk_command(interaction: Interaction):
    """
    csvファイルからランダムに一行選んで返す。
    :param interaction:
    :return:
    """
    await interaction.response.send_message("Random tikutiku message")

@app_commands.command(name="tktk_help", description="Show help for tikutiku bot")
async def tktk_help_command(interaction: Interaction):
    """
    ヘルプメッセージを返す。
    :param interaction:
    :return:
    """
    help_text = (
        "/tktk : Show a random tikutiku quote\n"
        "/tktk_help : Show this help message\n"
        "/tktk_settime <HH:MM> : Set reminder time\n"
        "/tktk_setchannel : Set reminder channel\n"
        "/tktk_reminder <on|off> : Toggle reminder"
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
    await interaction.response.send_message(f"Reminder time set to {time}")

@app_commands.command(name="tktk_setchannel", description="Set reminder channel")
async def tktk_setchannel_command(interaction: Interaction):
    """
    リマインダーのチャンネルを設定する。
    :param interaction:
    :return:
    """
    await interaction.response.send_message(f"Reminder channel set to {interaction.channel_id}")

@app_commands.command(name="tktk_reminder", description="Toggle reminder ON/OFF")
async def tktk_reminder_command(interaction: Interaction, onoff: str):
    """
    リマインダーのON/OFFを切り替える。
    :param interaction:
    :param onoff:
    :return:
    """
    await interaction.response.send_message(f"Reminder {'enabled' if onoff == 'on' else 'disabled'}")


def get_commands():
    return [
        tktk_command,
        tktk_help_command,
        tktk_settime_command,
        tktk_setchannel_command,
        tktk_reminder_command
    ]

