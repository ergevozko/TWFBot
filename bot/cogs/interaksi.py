import discord
from discord.ext import commands
import random
import config

class Interaksi(commands.Cog):

    def __init__(self, client):
        self.client = client


    # >teawaffle_hi/halo
    @commands.command(aliases=["halo"])
    async def hi(self, ctx):
        """ Menyapa bot """
        await ctx.send("Hi juga! Btw jangan ganggu dulu ya, lagi nonton VTuber idola nih!")

    @commands.command(aliases=["simper","ngesimp"])
    async def simp(self, ctx):
        """ Bot itu simp? """
        await ctx.send("Masalah ya? Emang bot ga bole ngesimp juga?")

    @commands.command(aliases=["test"])
    async def tes(self, ctx):
        """ Testing bot """
        await ctx.send("Ti... ga jadi 😝")

    @commands.command()
    async def iloveyou(self, ctx):
        """ Kirim cinta ke bot """
        await ctx.send(ctx.message.author.mention + " " + random.choice(config.tsundere))

    @commands.command(aliases=["meluk", "hug"])
    async def peluk(self, ctx, *, member: discord.Member = None):
        """Peluk seseorang di server <3"""
        try:
            if member is None:
                await ctx.send("Peluk erat kak " + ctx.message.author.mention + "!")
            else:
                if member.id == ctx.message.author.id:
                    await ctx.send("Kak " + ctx.message.author.mention + " meluk diri sendiri!")
                else:
                    await ctx.send("Kak" + member.mention + " dipeluk sama kak " + ctx.message.author.mention + "!")

        except:
            await ctx.send(config.err_msg_gtw)


def setup(client):
    client.add_cog(Interaksi(client))