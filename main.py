import os
import asyncio

import aiohttp
import discord
from discord import app_commands
from discord.ext import commands


TOKEN = os.getenv("DISCORD_TOKEN")

API_URL = "https://secure.pixelgunserver.com/pixelgun3d-config/getBanList.php"
CONFIG_URL = "https://cfg.pixelgun3d.com/config.json"

CACHE_TTL = 3600  # 1 hour
version_cache = {
    "version": None,
    "timestamp": 0,
}

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


async def fetch_version(session: aiohttp.ClientSession) -> str:
    now = asyncio.get_running_loop().time()

    if (
        version_cache["version"]
        and now - version_cache["timestamp"] < CACHE_TTL
    ):
        return version_cache["version"]

    async with session.get(CONFIG_URL) as response:
        response.raise_for_status()
        text = await response.text()

    version = text.strip('[]"')
    version_cache["version"] = version
    version_cache["timestamp"] = now

    return version


async def check_ban(session: aiohttp.ClientSession, player_id: str) -> str:
    version = await fetch_version(session)

    data = {
        "app_version": f"101:{version}",
        "ver": version,
        "platform": "101",
        "type_device": "1",
        "id": player_id,
    }

    async with session.post(API_URL, data=data) as response:
        result = (await response.text()).strip()

    if result == "1":
        return f"✅ User `{player_id}` **is banned**."
    if result == "0":
        return f"❌ User `{player_id}` **is not banned**."
    if result == "-1":
        return "⚠️ Special response (likely you are a developer)."
    if result == "File not found.":
        return "❌ The PHP file was deleted from the server."

    return "⚠️ Error: Pixel Gun configuration may have changed or servers are down."


@bot.event
async def on_ready():
    print(f"✅ Bot connected as {bot.user}")

    try:
        synced = await bot.tree.sync()
        print(f"Commands synced: {len(synced)}")
    except Exception as error:
        print(f"Error syncing commands: {error}")


@bot.tree.command(
    name="checkban",
    description="Check if a Player ID is banned in Pixel Gun 3D",
)
@app_commands.describe(player_id="Player ID to check")
async def checkban(interaction: discord.Interaction, player_id: str):
    await interaction.response.defer()

    try:
        async with aiohttp.ClientSession() as session:
            result = await check_ban(session, player_id)

        await interaction.followup.send(result)
    except Exception as error:
        await interaction.followup.send(f"❌ Error: {error}")


if __name__ == "__main__":
    if not TOKEN:
        raise RuntimeError("DISCORD_TOKEN environment variable is not set.")

    bot.run(TOKEN)
