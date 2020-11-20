# activate Birb

import discord

from redbot.core import commands
from random import randrange

BaseCog = getattr(commands, "Cog", object)

class Birb(BaseCog):
	"""Birb commands."""
	
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def aaa(self, ctx):
		"""screm"""
		screm_list1 = []
		num = 0
		x = randrange(1,50)
		screm = randrange(0,1)

		for num in x:
			if screm > 0:
				screm_list1.append('A')
			else:
				screm_list1.append('a')
		num += 1
		await ctx.send(''.join(screm_list1))

	def cog_unload(self):
		self.bot.loop.create_task(self.session.close())

	__del__ = cog_unload
