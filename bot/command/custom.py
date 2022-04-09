import discord
import os
import discord.ext
from discord.ext import commands

bot = commands.Bot(command_prefix="teawaffle?")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print("TWFBot random command ready!")
    print(f"Logged in as {bot.user.name}({bot.user.id})")
    
@bot.command()
async def ping(ctx):
    await ctx.send("pong?")
    
@bot.command()
async def hi(ctx):
    await ctx.send("Hi juga. Jangan ganggu ya plis! Lagi nonton VTuber idola nih!")
    
@bot.command()
async def halo(ctx):
    await ctx.send("Halo juga. Jangan ganggu ya plis! Lagi nonton VTuber idola nih!")

@bot.command()
async def simp(ctx):
    await ctx.send("Masalah? Emang bot ga bole nge-simp?")

@bot.command()
async def tes(ctx):
    await ctx.send("Ti... ga jadi 😝")

@bot.command()
async def love_you(ctx):
    await ctx.send("I... I hate you! BAKA!")
    
if __name__ == "__main__":
    bot.run(TOKEN)
