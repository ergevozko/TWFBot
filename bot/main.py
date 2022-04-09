import os
import discord.ext
from discord.ext import commands

bot = commands.Bot(command_prefix="teawaffle?")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")
    
activity = discord.Activity(name='VTuber', type=discord.ActivityType.watching)
client = discord.Client(activity=activity)

@bot.command()
async def ping(ctx):
    await ctx.send("pong!")

if __name__ == "__main__":
    bot.run(TOKEN)
