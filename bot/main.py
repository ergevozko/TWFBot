import discord
from discord.ext import commands
import sys
import os
import time


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
    """ Ping bot! """
    try:
        start_ping = time.time()
        message = await ctx.send("Eh...")
        end_ping = time.time()
        latency = client.latency
        embed = discord.embed(title="PING PONG!", description=f"**Latency**: {round(latency * 1000)}ms\n**Response time**: {round((end_ping - start_ping) * 1000)}ms", color=0xff6a3d)
        await message.edit(content=f"Oh... **Pong!**", embed = embed)
        print(f"Ada yang ngeping bot! Latensi/Response nya {round(latency * 1000)}/{round((end_ping - start_ping) * 1000)} ms")
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
