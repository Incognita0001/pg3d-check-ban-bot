# PG3D Check Ban Bot

A simple Discord bot that checks whether a Pixel Gun 3D player ID is currently banned.

## Features

* `/checkban` slash command
* Checks whether a Pixel Gun 3D Player ID is banned

## Requirements

* Python 3.10+
* `discord.py`
* `aiohttp`

## Installation

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

The bot token is read from the `DISCORD_TOKEN` environment variable.

### Windows PowerShell

Copy and paste the following commands into PowerShell:

```powershell
$env:DISCORD_TOKEN="YOUR_BOT_TOKEN"
python main.py
```

> Replace `YOUR_BOT_TOKEN` with your actual Discord bot token.

Do not put your Discord bot token directly in the source code.
