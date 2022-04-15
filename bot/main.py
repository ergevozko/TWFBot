import discord
import os
from discord.ext import commands
import time
import sys


# Config.py setup
if not os.path.isfile("config.py"):
    sys.exit("'config.py' tidak ditemukan!")
else:
    import config


TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=config.prefik, intents=intents, description=config.deskripsi)


@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}({client.user.id})")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="VTUBERS"))
    print("Bot is online")
    
@client.command()
async def ping(ctx):
    """ Nge-ping bot dapat response time. """
    try:
        pingtime = time.time()
        pingms = await ctx.send("*Eh...*")
        ping = (time.time() - pingtime) * 1000
        await client.edit_message(pingms, "Oh... **pong!** Btw ping responnya sekitar `%dms`" % ping)
        print("Seseorang nge-ping bot dengan response time %dms." % ping)
    except:
        await ctx.send(config.err_msg_gtw)

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    """ Menjalankan ekstensi """
    client.load_extension(f"bot.cogs.{extension}")

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    """ Mencopot ekstensi """
    client.unload_extension(f"bot.cogs.{extension}")

for filename in os.listdir(f"bot/cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"bot.cogs.{filename[:-3]}")

if __name__ == "__main__":
    client.run(TOKEN)
