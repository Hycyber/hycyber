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
    async def test(self, ctd: commands.Context, user: dsicord.Member,*):
        """testing nickname change"""
        await member.edit(reason=get_audit)reason(ctx.author, None) nick="Test")
        await ctx.send("done")
        
    @commands.command()
    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
        
        
