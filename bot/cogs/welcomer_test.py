import discord
from discord.ext import commands
from PIL import Image, ImageChops, ImageDraw, ImageFont
from io import BytesIO
import asyncio
import os
import datetime
import random
import numpy as np
    

class testWelcomer(commands.Cog):

    def __init__(self, client):
        self.client = client



    # Test Welcome Message trigger with command
    @commands.command()
    @commands.is_owner()
    async def testwelcome(self, ctx, user: discord.Member):
        text = "Halo"+user.mention+", selamat datang dan semoga betah di TeaWaffle!\n\nJangan lupa baca dulu peraturan server di 『 📜｜rules 』 » lalu perkenalkan dirimu di 『 👋｜introduction 』 » setelah itu pilih roles agar bisa berinteraksi dan dapat informasi menarik lainnya di 『 🥇｜get-roles 』"
        useravatar = user.avatar_url_as(size=1024)  # Profilepicture = member.avatar_url_as(size=500)
        datavatar = BytesIO(await useravatar.read())
        avatar = Image.open(datavatar)

        #make avatar circle
        bigsize = (avatar.size[0] * 3, avatar.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(avatar.size, Image.ANTIALIAS)
        mask = ImageChops.darker(mask, avatar.split()[-1])
        avatar.putalpha(mask)
        avatar = avatar.resize((240,240), Image.ANTIALIAS).convert("RGBA")

        img = Image.open("bot/resources/welcomer/twfcard.png")
        draw = ImageDraw.Draw(img)
        msgtop = "{} just joined the server".format(user.name)
        msgtopfont = ImageFont.truetype("bot/resources/welcomer/shentox-medium.otf", 42)
        wt, ht = draw.textsize(msgtop, msgtopfont)
        msgbot = ("Member #" + str(ctx.guild.member_count))
        msgbotfont = ImageFont.truetype("bot/resources/welcomer/shentox-medium.otf", 28)
        wb, hb = draw.textsize(msgbot, msgbotfont)
        draw.text(( (img.width - wt)/2, 340), msgtop, (255, 255, 255), font=msgtopfont)
        draw.text(( (img.width - wb)/2, 400), msgbot, (136, 136, 136), font=msgbotfont)

        img.paste(avatar, (430,70), avatar)

        with BytesIO() as image_binary:
            img.save(image_binary, 'PNG')
            image_binary.seek(0)
            await ctx.send(file=discord.File(fp=image_binary, filename='card.png'))

def setup(client):
    client.add_cog(testWelcomer(client))
