import os
import discord.ext
from discord.ext import commands
from .context import CustomContext

bot = commands.Bot(command_prefix="teawaffle?")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print("TWFBot random command ready!")
    print(f"Logged in as {bot.user.name}({bot.user.id})")
    
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

# @bot.command()
# async def love_you(ctx):
#    await ctx.send("I... I hate you! BAKA!")
    
class Bot(commands.Bot):
	"""A subclass of commands.Bot, useful for creating custom context."""
	async def get_context(self, message, *, cls = CustomContext):
		return await super().get_context(message, cls = cls)
    
class CustomContext(commands.Context):
	"""An extended context to use in commands."""
	async def love_you(self):
		await self.send("I... I hate you! BAKA!")
    
if __name__ == "__main__":
    bot.run(TOKEN)
