# 補助関数
import json
import os

SETTINGS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'env', 'settings.json')

def load_settings():
    """Load settings from settings.json."""
    if not os.path.exists(SETTINGS_PATH):
        return {
            "reminder_time": "08:00",
            "reminder_channel": None,
            "reminder_enabled": False
        }
    with open(SETTINGS_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_settings(settings):
    """Save settings to settings.json."""
    with open(SETTINGS_PATH, 'w', encoding='utf-8') as f:
        json.dump(settings, f, ensure_ascii=False, indent=2)


def load_json():
    """
    JSONファイルを読み込み、Pythonの辞書型に変換する関数
    :return: JSONデータを含む辞書型オブジェクト
    """
    with open(SETTINGS_PATH, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def load_guild_settings(guild_id):
    """指定ギルドの設定を取得。なければデフォルト値を返す"""
    all_settings = load_settings()
    return all_settings.get(str(guild_id), {
        "reminder_time": "08:00",
        "reminder_channel": None,
        "reminder_enabled": False
    })


def save_guild_settings(guild_id, settings):
    """指定ギルドの設定を保存。全体のsettings.jsonを更新"""
    all_settings = load_settings()
    all_settings[str(guild_id)] = settings
    save_settings(all_settings)
