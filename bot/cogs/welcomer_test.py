import discord
import os

from discord.ext import commands
from PIL import Image, ImageOps, ImageDraw, ImageFont
from io import BytesIO
    
class TesWelcomer(commands.Cog, description = "Ngetes 'Pesan Selamat Datang' via perintah bot"):

    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["welcomer_tes"])
    @commands.is_owner()
    async def tes_welcomer(self, ctx, user: discord.Member):
        """Perintah uji coba Pesan Selamat Datang"""
        # Pesan selamat datang
        text = "Halo "+user.mention+", selamat datang dan semoga betah di TeaWaffle!\n\nJangan lupa baca dulu peraturan server di『 <#903295887692943361> 』» lalu perkenalkan dirimu di『 <#959261466966519808> 』» setelah itu pilih roles agar bisa berinteraksi dan dapat informasi menarik lainnya di『 <#959829754356322304> 』"
        # Mendapatkan avatar member
        useravatar = user.avatar_url_as(size=1024)
        datavatar = BytesIO(await useravatar.read())
        avatar = Image.open(datavatar)
        # Membuat avatar berbentuk lingkaran
        bigsize = (avatar.size[0] * 3, avatar.size[1] * 3)
        mask = Image.new("L", bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(avatar.size, Image.ANTIALIAS)
        avatar.putalpha(mask)
        cavatar = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
        cavatar.putalpha(mask)
        avatar = avatar.resize((240,240), Image.ANTIALIAS).convert("RGBA")
        # Membuat background
        img = Image.open("bot/assets/welcomer/twfcard.png")
        draw = ImageDraw.Draw(img)
        msgtop = (str(user) + " just joined the server")
        msgtopfont = ImageFont.truetype("bot/assets/welcomer/shentox-medium.otf", 42)
        wt, ht = draw.textsize(msgtop, msgtopfont)
        msgbot = ("Member #" + str(ctx.guild.member_count))
        msgbotfont = ImageFont.truetype("bot/assets/welcomer/shentox-medium.otf", 30)
        wb, hb = draw.textsize(msgbot, msgbotfont)        
        draw.text( ((img.width - wt)/2, 330), msgtop, (255, 255, 255), font=msgtopfont )
        draw.text( ((img.width - wb)/2, 400), msgbot, (136, 136, 136), font=msgbotfont )
        # Pasang avatar ke background
        img.paste(avatar, (430,70), avatar)
        # Mengirim hasil jadi Kartu Selamat Datang
        with BytesIO() as image_binary:
            img.save(image_binary, "PNG")
            image_binary.seek(0)
            await ctx.send(file=discord.File(fp=image_binary, filename="card.png"), content=text)


def setup(client):
    client.add_cog(TesWelcomer(client))