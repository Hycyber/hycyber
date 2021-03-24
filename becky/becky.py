# activate becky

import discord

from redbot.core import commands
from random import randrange

BaseCog = getattr(commands, "Cog", object)

class Becky(BaseCog):
    """Becky commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def becky(self, ctx):
        """becky quotes"""
        becky_list =[]
        becky = ["This is a nice stick",
                 "I like sticks",
                 "Peck",
                 "Peck",
                 "No Ron, go find Becky",
                 "No Ron, I don't want sum fuk",
                 "Ugh",
                 "Ron, your tail is small",
                 "Ron, I'm leaving"]
        
        num = 0
        range = randrange(1,15)

        for num in xrange(range):
            bird = random.randint(0,1)
            if bird > 0:
                becky_list.append(random.choice(becky))
                becky_list.append('\n')
            else:
                becky_list.append('stik')
                becky_list.append('\n')

        await ctx.send(''.join(becky_list))
    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def becky(self, ctx):
        """becky quotes"""
        becky_list =[]
        becky = ["This is a nice stick",
                 "I like sticks",
                 "Peck",
                 "Peck",
                 "No Ron, go find Becky",
                 "No Ron, I don't want sum fuk",
                 "Ugh",
                 "Ron, your tail is small",
                 "Ron, I'm leaving"]
        num = 0
        range = randrange(1,15)

        for num in xrange(range):
            bird = random.randint(0,1)
            if bird > 0:
                becky_list.append(random.choice(becky))
                becky_list.append('\n')
            else:
                becky_list.append('stik')
                becky_list.append('\n')

        await ctx.send(''.join(becky_list))
    @commands.command()
    
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def ron(self, ctx):
        """ron quotes"""
        ron_list =[]
        ron = ["Lemme smash",
               "Please",
               "You want, sum fuk?",
               "I got you blue",
               "Hey gurl, you want some tail?",
               "Wot?",
               "Swiggity, swooty",
               "You want yellow?",
               "She doesn't want yellow",
               "Blue and yellow?",
               "Wut?",
               "No wait lemme smash",
               "What has my life come to?",
               "Becky thought my tail was big",
               "Becky used to let me smash. But Becky is smashing Ben",
               "Ben is a hoe",
               "FUCK THIS NEST, FUCK BEN",
               "I NEED YOU BECKY",
               "BECKY LEMME SMASH",
               "Imma get that bitch a stick. Bitches love sticks",
               "Wrong stick",
               "Stick",
               "Need stick",
               "Got stick",
               "Becky, I got stick",
               "LEMME SMASH"]
        num = 0
        range = randrange(1,15)

        for num in xrange(range):
            bird = random.randint(0,1)
            if bird > 0:
                ron_list.append(random.choice(ron))
                ron_list.append('\n')
            else:
                ron_list.append('stik')
                ron_list.append('\n')

        await ctx.send(''.join(ron_list))
    @commands.command()

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
        
        
