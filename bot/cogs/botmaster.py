import time
import aiohttp
import discord
import importlib
import os
import sys

from discord.ext import commands
from utils import permissions, default, http


class BotMaster(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog `BotMaster` berhasil dijalankan!")


    @commands.command()
    @commands.check(permissions.is_botmaster)
    async def load(self, ctx, ekstensi: str):
        """Mengaktifkan ekstensi"""
        try:
            self.bot.load_extension(f"bot.cogs.{ekstensi}")
        except Exception as e:
            return await ctx.send(default.traceback_maker(e))
        await ctx.send(f"**{ekstensi}.py** diaktifkan!")


    @commands.command()
    @commands.check(permissions.is_botmaster)
    async def unload(self, ctx, ekstensi: str):
        """Menonaktifkan ekstensi"""
        try:
            self.bot.unload_extension(f"bot.cogs.{ekstensi}")
        except Exception as e:
            return await ctx.send(default.traceback_maker(e))
        await ctx.send(f"**{ekstensi}.py** dinonaktifkan")


    @commands.command()
    @commands.check(permissions.is_botmaster)
    async def reload(self, ctx, ekstensi: str):
        """Pengaktifan ulang ekstensi"""
        try:
            self.bot.reload_extension(f"cogs.{ekstensi}")
        except Exception as e:
            return await ctx.send(default.traceback_maker(e))
        await ctx.send(f"**{ekstensi}.py** diaktifkan ulang")


    @commands.command()
    @commands.check(permissions.is_botmaster)
    async def reloadall(self, ctx):
        """Reloads semua ekstensi"""
        error_collection = []
        for file in os.listdir("bot/cogs"):
            if file.endswith(".py"):
                name = file[:-3]
                try:
                    self.bot.reload_extension(f"bot.cogs.{name}")
                except Exception as e:
                    error_collection.append(
                        [file, default.traceback_maker(e, advance=False)]
                    )

        if error_collection:
            output = "\n".join([f"**{g[0]}** ```diff\n- {g[1]}```" for g in error_collection])
            return await ctx.send(
                f"Berhasil reload semua ekstensi,"
                f"namun beberapa ekstensi gagal reload...\n\n{output}"
            )

        await ctx.send("Berhasil reload semua ekstensi")


    @commands.command()
    @commands.check(permissions.is_botmaster)
    async def reloadutils(self, ctx, name: str):
        """Reloads modul utils"""
        name_maker = f"bot/utils/{name}.py"
        try:
            module_name = importlib.import_module(f"bot.utils.{name}")
            importlib.reload(module_name)
        except ModuleNotFoundError:
            return await ctx.send(f"Tidak dapat menemukan modul dengan nama **{name_maker}**")
        except Exception as e:
            error = default.traceback_maker(e)
            return await ctx.send(f"Modul **{name_maker}** error dan gagal reload...\n{error}")
        await ctx.send(f"Modul **{name_maker}** berhasil reload")


    @commands.command()
    @commands.check(permissions.is_botmaster)
    async def reboot(self, ctx):
        """Bot reboot"""
        await ctx.send("Bot rebooting...")
        time.sleep(1)
        sys.exit(0)


    @commands.group()
    @commands.check(permissions.is_botmaster)
    async def change(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send_help(str(ctx.command))


    @commands.command()
    @commands.check(permissions.is_botmaster)
    async def dm(self, ctx, user: discord.User, *, message: str):
        """DM user"""
        try:
            await user.send(message)
            await ctx.send(f"✉️ Mengirimkan DM ke **{user}**")
        except discord.Forbidden:
            await ctx.send("Pengguna ini mungkin memblokir DM atau akun bot...")


    @change.command(name="username")
    @commands.check(permissions.is_botmaster)
    async def change_username(self, ctx, *, name: str):
        """Mengganti username"""
        try:
            await self.bot.user.edit(username=name)
            await ctx.send(f"Berhasil mengganti username menjadi **{name}**")
        except discord.HTTPException as err:
            await ctx.send(err)


    @change.command(name="nickname")
    @commands.check(permissions.is_botmaster)
    async def change_nickname(self, ctx, *, name: str = None):
        """Mengganti nickname"""
        try:
            await ctx.guild.me.edit(nick=name)
            if name:
                await ctx.send(f"Berhasil mengganti nickname menjadi **{name}**")
            else:
                await ctx.send("Berhasil menghapus nickname")
        except Exception as err:
            await ctx.send(err)


    @change.command(name="avatar")
    @commands.check(permissions.is_owner)
    async def change_avatar(self, ctx, url: str = None):
        """Mengganti avatar"""
        if url is None and len(ctx.message.attachments) == 1:
            url = ctx.message.attachments[0].url
        else:
            url = url.strip("<>") if url else None

        try:
            bio = await http.get(url, res_method="read")
            await self.bot.user.edit(avatar=bio)
            await ctx.send(f"Berhasil mengganti avatar. Sementara menggunakan:\n{url}")
        except aiohttp.InvalidURL:
            await ctx.send("URL tidak valid")
        except discord.InvalidArgument:
            await ctx.send("URL ini tidak berisi gambar yang bisa digunakan")
        except discord.HTTPException as err:
            await ctx.send(err)
        except TypeError:
            await ctx.send("Kamu harus menyantumkan URL gambar atau mengunggahnya dengan perintah")


async def setup(bot):
    await bot.add_cog(BotMaster(bot))