# らいじんチクチクBot

「らいさまチクチク名言集」からランダムに名言を引用するDiscord Bot。毎朝任意の時間に名言をリマインドする機能も搭載。

## 機能

| コマンド               | 機能              | 説明                            |
|--------------------|-----------------|-------------------------------|
| `/tktk`            | 名言を引用           | 「らいさまチクチク名言集」からランダムに名言を引用します。 |
| `/tktk help`       | ヘルプを表示          | Botの使い方を表示します。                |
| `/tktk reminder`   | リマインダー機能のON/OFF | 毎朝任意の時間にチャットされる機能のON/OFF      |
| `/tktk settime`    | リマインダー時間の設定     | 毎朝のリマインダー時間を設定します。            |
| `/tktk setchannel` | リマインダー送信先の設定    | リマインダーを送信するチャンネルを設定します。       |

## requirements

- Python 3.13

## プロジェクト構成

```
DiscordBot_TIKUTIKU/
├── bot.py                # メインBotプログラム
├── config.py             # 設定（トークン、リマインダー時間等）
├── quotes.csv            # 名言集（CSV形式）
├── reminder.py           # リマインダー機能のロジック
├── commands.py           # コマンド処理（/tktk, /tktk help等）
├── utils.py              # 補助関数（CSV読み込み等）
├── requirements.txt      # 必要なPythonパッケージ
├── README.md             # 説明書
├── .gitignore            # Gitで管理しないファイル
├── .env/                 # 仮想環境
└── docs/                 # ドキュメント
```

## Reference

- [Pythonで実用Discord Bot](https://qiita.com/1ntegrale9/items/9d570ef8175cf178468f)
- [らいさまちくちく集_2025-10-12](https://docs.google.com/spreadsheets/d/1TCR4HoYr2zURLk5cMeZWHtN6eW0LorvNT7EV7wUu7Ek/edit?gid=0#gid=0)

