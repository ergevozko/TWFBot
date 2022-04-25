import discord
import random
import config

from discord.ext import commands


class Interaksi(commands.Cog):

    def __init__(self, client):
        self.client = client


    # >teawaffle_hi/halo
    @commands.command(aliases=["halo"])
    async def hi(self, ctx):
        """Menyapa bot"""
        await ctx.send("Yo! Sebentar ya, lagi nonton VTuber kesayangan nih!")


    @commands.command(aliases=["simper","ngesimp"])
    async def simp(self, ctx):
        """Bot itu simp?"""
        await ctx.send("Masalah ya? Emang bot ga bole ngesimp juga?")


    @commands.command(aliases=["test"])
    async def tes(self, ctx):
        """Testing bot"""
        await ctx.send("Ti... ga jadi 😝")


    @commands.command(aliases=["love"])
    async def iloveyou(self, ctx):
        """Kirim cinta ke bot"""
        BOTRESP = [
            "Hee? Ada-ada aja kamu kak",
            "Ah masa? Bercanda pasti nih!!"
        ]
        await ctx.send(ctx.message.author.mention + " " + random.choice(BOTRESP))


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
            await ctx.send(config.ERR_MSG_GENERIC)


    @commands.command(aliases=["8bola","boladelapan","8ball", "eightball"])
    async def bola8(self, ctx, *, question: commands.clean_content):
        """Konsolutasi 8bola"""
        BOTRESP = [
            "It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely", "You may rely on it", "As i see it, yes", "Most likely",
            "Outlook good", "Yes", "Signs point to yes", "Reply haze, try again", "Ask again later", "Better not tell you now", "Cannot predict now",
            "Concentrate and ask again", "Do not count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"
        ]
        answer = random.choice(ballresponse)
        await ctx.send(f"🎱 **Pertanyaan:** {question}\n**Jawaban:** {answer}")


def setup(client):
    client.add_cog(Interaksi(client))