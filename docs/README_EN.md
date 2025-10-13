# Raijin Chikutiku Bot

A Discord Bot that randomly quotes from the "Raijin Chikutiku Quotes Collection". It also features a daily reminder function at a user-specified time.

## Features

| Command            | Function             | Description                                                    |
|--------------------|----------------------|----------------------------------------------------------------|
| `/tktk`            | Quote                | Randomly quotes from the "Raijin Chikutiku Quotes Collection". |
| `/tktk help`       | Show help            | Displays instructions for using the bot.                       |
| `/tktk reminder`   | Reminder ON/OFF      | Toggles the daily reminder feature.                            |
| `/tktk settime`    | Set reminder time    | Sets the time for the daily reminder.                          |
| `/tktk setchannel` | Set reminder channel | Sets the channel to send reminders to.                         |

## Requirements

- Python 3.13

## Project Structure

```
DiscordBot_TIKUTIKU/
├── bot.py                # Main bot program
├── config.py             # Settings (token, reminder time, etc.)
├── quotes.csv            # Quotes collection (CSV format)
├── reminder.py           # Reminder logic
├── commands.py           # Command handling (/tktk, /tktk help, etc.)
├── utils.py              # Utility functions (CSV reading, etc.)
├── requirements.txt      # Required Python packages
├── README.md             # Documentation
├── .gitignore            # Files not tracked by Git
├── .env/                 # Virtual environment
└── docs/                 # Additional documents
```

## Reference

- [Practical Discord Bot with Python](https://qiita.com/1ntegrale9/items/9d570ef8175cf178468f)
- [Raijin Chikutiku Collection_2025-10-12](https://docs.google.com/spreadsheets/d/1TCR4HoYr2zURLk5cMeZWHtN6eW0LorvNT7EV7wUu7Ek/edit?gid=0#gid=0)
