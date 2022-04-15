import discord
from discord.ext import commands

class Interaksi(commands.Cog):

    """ Perintah bot untuk berinteraksi """

    def __init__(self, client):
        self.client = client

    # >teawaffle_hi
    @commands.command()
    async def hi(self, ctx):
        await ctx.send("Hi juga! Btw jangan ganggu dulu ya, lagi nonton VTuber idola nih!")

    # >teawaffle_halo
    @commands.command()
    async def halo(self, ctx):
        await ctx.send("Halo juga! Btw jangan ganggu dulu ya, lagi nonton VTuber idola nih!")

    # >teawaffle_simp
    @commands.command()
    async def simp(self, ctx):
        await ctx.send("Masalah ya? Emang bot ga bole nge-simp juga?")

    # >teawaffle_tes
    @commands.command()
    async def tes(self, ctx):
        await ctx.send("Ti... ga jadi 😝")

    # >teawaffle_iloveyou
    @commands.command()
    async def iloveyou(self, ctx):
        await ctx.send("I... I hate you! BAKA!")

def setup(client):
    client.add_cog(Interaksi(client))
