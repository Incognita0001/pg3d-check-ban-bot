# PG3D Check Ban Bot

A simple Discord bot that checks whether a Pixel Gun 3D Player ID is currently banned.

## Features

- `/checkban` slash command
- Checks the Pixel Gun 3D ban list
- Automatically fetches the current game version
- Caches the game version for 1 hour

## Requirements

- Python 3.10+
- `discord.py`
- `aiohttp`

## Installation

Install the dependencies:

```bash
pip install -r requirements.txt
## Configuration

The bot token is read from the `DISCORD_TOKEN` environment variable.

### Windows PowerShell

```powershell
$env:DISCORD_TOKEN="YOUR_BOT_TOKEN"
python main.py
```

### Windows CMD

```cmd
set DISCORD_TOKEN=YOUR_BOT_TOKEN
python main.py
```
Do not put your Discord bot token directly in the source code.
