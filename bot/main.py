import os
import discord.ext
from discord.ext import commands

bot = commands.Bot(command_prefix="teawaffle?")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="VTUBERS"))
    print(f"Logged in as {bot.user.name}({bot.user.id})")
    
@bot.command()
async def ping(ctx):
    await ctx.send("pong?")

if __name__ == "__main__":
    bot.run(TOKEN)
