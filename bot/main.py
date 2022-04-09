import discord
import os
from command import custom 

client = discord.Client()
TOKEN = os.getenv("DISCORD_TOKEN")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="VTUBERS"))
    print(f"Logged in as {client.user.name}({client.user.id})")

if __name__ == "__main__":
    client.run(TOKEN)
