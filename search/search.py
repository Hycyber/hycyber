#Encompassing search cog

import discord
import aiohttp
import requests
import random


from redbot.core import commands

BaseCog = getattr(commands, "Cog", object)

class IMG(BaseCog):
    """Cog used as a search function for multiple commands"""

    def __init__(self, bot):
        self.bot = bot

#Requested by Kira
  #!fert
    @commands.command()
    async def fert(self, ctx):

        search = "ferret"

        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.qwant.com/api/search/images") as r:

                params={
                    'count': 50,
                    'q': search,
                    't': 'images',
                    'safesearch': 1,
                    'locale': 'en_US',
                    'uiv': 4
                },
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
                }

                response = r.json().get('data').get('result').get('items')
                urls = [r.get('media') for r in response]

                await ctx.send(random.choice(urls))

    def setup(bot):
        bot.add_cog(IMG(bot))
