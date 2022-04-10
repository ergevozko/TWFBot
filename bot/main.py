import discord
import os
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")
client = commands.Bot(command_prefix=">teawaffle_")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="VTUBERS"))
    print(f"Logged in as {client.user.name}({client.user.id})")

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('../cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs{filename[:-3]}')

if __name__ == "__main__":
    client.run(TOKEN)
