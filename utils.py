# 補助関数
import json
import os

SETTINGS_PATH = os.path.join(os.path.dirname(__file__), 'settings.json')

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


def load_json(file_path):
    """
    JSONファイルを読み込み、Pythonの辞書型に変換する関数
    :param file_path: 読み込むJSONファイルのパス
    :return: JSONデータを含む辞書型オブジェクト
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data