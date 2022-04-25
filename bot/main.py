import discord
import sys
import os
import time

from discord.ext import commands
from utils import default
from utils.data import Bot, HelpFormat


# Config.py setup
if not os.path.isfile("config.py"):
    sys.exit("'config.py' tidak ditemukan!")
else:
    import config


client = commands.Bot(
    command_prefix=config.PREFIX, prefix=config.PREFIX, description=config.BOT_DESC,
    owner_ids=config.BOT_MASTER, command_attrs=dict(hidden=True), help_command=HelpFormat(),
    allowed_mentions=discord.AllowedMentions(roles=False, users=True, everyone=False),
    intents=discord.Intents(
        # kwargs found at https://docs.pycord.dev/en/master/api.html?highlight=discord%20intents#discord.Intents
        guilds=True, members=True, messages=True, reactions=True, presences=True
    )
)


@client.event
async def on_ready():
    print("Bot sudah online!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=config.BOT_WATCH))
    print(f"Terdaftar di {client.guild.name} sebagai {client.user.name} [ {client.user.id} ]")


for filename in os.listdir(f"bot/cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"bot.cogs.{filename[:-3]}")


if __name__ == "__main__":
    client.run(config.BOT_TOKEN)
