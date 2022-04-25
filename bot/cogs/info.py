import time
import discord
import psutil
import os
import config

from discord.ext import commands
from utils import default, http


class Informasi(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog `Informasi` berhasil dijalankan!")


    @commands.command()
    async def ping(self, ctx):
        """Ping bot!"""
        try:
            start = time.time()
            message = await ctx.send(content="Eh...", embed=None)
            end = time.time()
            ping = (end - start) * 1000
            latency = client.latency * 1000
            embed = discord.Embed(title="PING PONG!", description=f"**Latency**: {round(latency)}ms\n**Response time**: {round(ping,2)}ms", color=config.BOT_COLOR)
            await message.edit(content="Oh... **Pong!**", embed=embed)
            print(f"Pinging bot dengan Latensi/Response: {round(latency)}/{round(ping)} ms")
        except:
            await ctx.send(config.ERR_MSG_GENERIC)


async def setup(bot):
    await bot.add_cog(Informasi(bot))