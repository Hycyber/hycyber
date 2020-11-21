# activate Turk

import discord

from redbot.core import commands
from random import randrange

BaseCog = getattr(commands, "Cog", object)

class Turk(BaseCog):
    """Turk commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def test(self, ctx, member: discord.Member):
        """testing nickname change"""
        await member.edit(nick = "test")
        
    @commands.command()
    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
        
        