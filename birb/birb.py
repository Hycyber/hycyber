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
	async def screm(self, ctx):
		"""screm"""
		screm_list1 = []
		num = 0
		x = randrange(1,200)
		screm = randrange(0,2)

		for num in range(0,x):
			if screm > 0:
				screm_list1.append('A')
			else:
				screm_list1.append('a')
		await ctx.send(''.join(screm_list1))
		
	@commands.command()
	async def aaa(self, ctx):
		"""screm"""
		screm_list1 = []
		num = 0
		x = randrange(1,200)

		for num in range(0,x):
			y = randrange(0,2)
			if y > 0:
				screm_list1.append('A')
			else:
				screm_list1.append('a')
		await ctx.send(''.join(screm_list1))
		
	@commands.command()
	async def boomer(self, ctx):
		"""boomer command requested by plague"""
		boomer = []
		num = 0
		x = randrange(2,200)
		
		boomer.append("B")

		for num in range(0,x):
			y = randrange(0,2)
			if(y > 0):
				boomer.append("O")
			else:
				boomer.append("o")
		boomer.append("MER")
		await ctx.send(''.join(boomer))
		

	def cog_unload(self):
		self.bot.loop.create_task(self.session.close())

	__del__ = cog_unload
