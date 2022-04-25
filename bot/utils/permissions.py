import discord
import config

from discord.ext import commands
from utils import default


BOTMASTER = config.BOT_MASTER


def is_botmaster(ctx):
    """Checks if the author is one of the bot master"""
    return ctx.author.id in BOTMASTER


async def check_permissions(ctx, perms, *, check=all):
    """"Checks if author has permissions to a permission"""
    if ctx.author.id in BOTMASTER:
        return True

    resolved = ctx.channel.permissions_for(ctx.author)
    return check(getattr(resolved, name, None) == value for name, value in perms.items())


def has_permissions(*, check=all, **perms):
    """discord.Commands method to check if author has permissions"""
    async def pred(ctx):
        return await check_permissions(ctx, perms, check=check)
    return commands.check(pred)


async def check_priv(ctx, member):
    """Custom (weird) way to check permissions when handling moderation commands"""
    try:
        # Self checks
        if member.id == ctx.author.id:
            return await ctx.send(f"Loh? Gak dibolehin {ctx.command.name} dirimu sendiri kak")
        if member.id == ctx.bot.user.id:
            return await ctx.send("Jadi ini yang kamu mau kak? Jahat! ;-;")

        # Check if user bypasses
        if ctx.author.id == ctx.guild.owner.id:
            return False

        # Now permission check
        if member.id in owners:
            if ctx.author.id not in owners:
                return await ctx.send(f"Maaf kak, gak bisa {ctx.command.name} penciptaku kak... ;-;")
            else:
                pass
        if member.id == ctx.guild.owner.id:
            return await ctx.send(f"Maaf kak, gak bisa {ctx.command.name} owner kak... wkwk")
        if ctx.author.top_role == member.top_role:
            return await ctx.send(f"Maaf kak, role yang sama gak bisa saling {ctx.command.name} kak...")
        if ctx.author.top_role < member.top_role:
            return await ctx.send(f"Maaf kak, gak bisa {ctx.command.name} karna role dia lebih tinggi...")
    except Exception:
        pass


def can_handle(ctx, permission: str):
    """ Checks if bot has permissions or is in DMs right now """
    return isinstance(ctx.channel, discord.DMChannel) or getattr(ctx.channel.permissions_for(ctx.guild.me), permission)