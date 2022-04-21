import discord
import sys
import os
import time

from discord.ext import commands
from bot.utils import permissions


# Config.py setup
if not os.path.isfile("config.py"):
    sys.exit("'config.py' tidak ditemukan!")
else:
    import config


client = commands.Bot(
    command_prefix=config.PREFIX,
    description=config.BOT_DESC,
    intents=discord.Intents(  # kwargs found at https://docs.pycord.dev/en/master/api.html?highlight=discord%20intents#discord.Intents
        guilds=True, members=True, messages=True, reactions=True, presences=True, message_content=True,
    )
)


@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}({client.user.id})")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=config.BOT_WATCH))
    print("Bot is online")


@client.command()
async def ping(ctx):
    """Ping bot!"""
    try:
        start = time.time()
        message = await ctx.send(content="Eh...", embed=None)
        end = time.time()
        ping = (end - start) * 1000
        latency = client.latency * 1000
        embed = discord.Embed(title="PING PONG!", description=f"**Latency**: {round(latency)}ms\n**Response time**: {round(ping,2)}ms", color=0xFF6A3D)
        await message.edit(content="Oh... **Pong!**", embed=embed)
        print(f"Pinging bot dengan Latensi/Response: {round(latency)}/{round(ping)} ms")
    except:
        await ctx.send(config.ERR_MSG_GENERIC)


@client.command(hidden=True)
@commands.check(permissions.is_botmaster)
async def load(ctx, ekstensi):
    """Mengaktifkan ekstensi"""
    client.load_extension(f"bot.cogs.{ekstensi}")
    print(f"Cogs '{ekstensi}' diaktifkan!")


@client.command(hidden=True)
@commands.check(permissions.is_botmaster)
async def unload(ctx, ekstensi):
    """Menonaktifkan ekstensi"""
    client.unload_extension(f"bot.cogs.{ekstensi}")
    print(f"Cogs '{ekstensi}' dinonaktifkan!")


for filename in os.listdir(f"bot/cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"bot.cogs.{filename[:-3]}")


if __name__ == "__main__":
    client.run(config.BOT_TOKEN)
