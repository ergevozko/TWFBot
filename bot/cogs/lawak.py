import discord
from discord.ext import commands

class Lawak(commands.Cog):

    def __init__(self, client):
        self.client = client

    # >teawaffle_ping
    @command.command()
    async def ping(self, ctx):
        await ctx.send("pong?")

    # >teawaffle_hi
    @command.command()
    async def hi(self, ctx):
        await ctx.send("Hi juga. Jangan ganggu ya plis! Lagi nonton VTuber idola nih!")

    # >teawaffle_halo
    @command.command()
    async def halo(self, ctx):
        await ctx.send("Halo juga. Jangan ganggu ya plis! Lagi nonton VTuber idola nih!")

    # >teawaffle_simp
    @command.command()
    async def simp(self, ctx):
        await ctx.send("Masalah? Emang bot ga bole nge-simp?")

    # >teawaffle_tes
    @command.command()
    async def tes(self, ctx):
        await ctx.send("Ti... ga jadi 😝")

    # >teawaffle_iloveyou
    @command.command()
    async def iloveyou(self, ctx):
        await ctx.send("I... I hate you! BAKA!")

def setup(client):
    client.add_cog(Lawak(client))
