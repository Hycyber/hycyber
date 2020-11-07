# activate Birb

import discord

from redbot.core import commands
from random import randrange

BaseCog = getattr(commands, "Cog", object)

class Birb(BaseCog):
    """Birb commands."""

    @commands.command()
    async def aaa(self, ctx):
        """screm"""
        screm_list = []
        num = 0
        range = randrange(1,50)
        screm = random.randint(0,1)

        for num in xrange(range):
            if screm > 0:
                screm_list.append('A')
            else:
                screm_list.append('a')
        await ctx.send(''.join(screm_list))
        
    @commands.command()
    async def screm(self, ctx):
        """screm but more typing"""
        screm_list = []
        num = 0
        range = randrange(1,50)
        screm = random.randint(0,1)

        for num in xrange(range):
            if screm > 0:
                screm_list.append('A')
            else:
                screm_list.append('a')
        await ctx.send(''.join(screm_list))

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
