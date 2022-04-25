import discord
import time
import traceback
from datetime import datetime
from io import BytesIO


def traceback_maker(err, advance: bool = True):
    """ A way to debug your code anywhere """
    _traceback = ''.join(traceback.format_tb(err.__traceback__))
    error = ('```py\n{1}{0}: {2}\n```').format(type(err).__name__, _traceback, err)
    return error if advance else f"{type(err).__name__}: {err}"


def timetext(name):
    """Timestamp, but in text form"""
    return f"{name}_{int(time.time())}.txt"


def date(target, clock: bool = True, seconds: bool = False, ago: bool = False, only_ago: bool = False):
    if isinstance(target, int) or isinstance(target, float):
        target = datetime.utcfromtimestamp(target)

    unix = int(time.mktime(target.timetuple()))
    timestamp = f"<t:{unix}:{'f' if clock else 'D'}>"
    if ago:
        timestamp += f" (<t:{unix}:R>)"
    if only_ago:
        timestamp = f"<t:{unix}:R>"
    return timestamp


def responsible(target, reason):
    """Default responsible maker targeted to find user in AuditLogs"""
    responsible = f"[ {target} ]"
    if not reason:
        return f"{responsible} alasan tidak ada"
    return f"{responsible} {reason}"


def actionmessage(case, mass=False):
    """Default way to present action confirmation in chat"""
    output = f"**{case}** user"

    if mass:
        output = f"**{case}** IDs/Users"

    return f"✅ {output} sukses!"


async def prettyResults(ctx, filename: str = "Hasil", resultmsg: str = "Berikut hasilnya:", loop=None):
    """A prettier way to show loop results"""
    if not loop:
        return await ctx.send("Tidak ada hasil yang ditemukan...")

    pretty = "\r\n".join([f"[{str(num).zfill(2)}] {data}" for num, data in enumerate(loop, start=1)])

    if len(loop) < 15:
        return await ctx.send(f"{resultmsg}```ini\n{pretty}```")

    data = BytesIO(pretty.encode('utf-8'))
    await ctx.send(
        content=resultmsg,
        file=discord.File(data, filename=timetext(filename.title()))
    )