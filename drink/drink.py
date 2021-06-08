#activate search DrinkOptions

import discord
import random

from .drinkoptions import DrinkOptions
from redbot.comre import commands
from random import randrange

BaseCog = getattr(commands, "Cog", object)

class Drink(BaseCog):

	#!liqa
	#Arguments (String type of liquor, e.g. !liqa whiskey)
	#Can be left empty for random choice out of all possible options

	#TODO:
		# argument for specific category
		# suggestion implementation to be tied to bot profile
		# potential? google search engine api to allow for more relevant stores nearby
		# international integration for overseas users

	@commands.command()
	async def liqa(self, ctx):
		"""tells you what to get from the store"""
		
		self.options = DrinkOptions()
		drink_list =[]
		
		drink_list.append("Currently in beta, suggestions to come later")
		drink_list.append('\n')
		
		x = randrange(1,11)

		if(x == 1):
			drink_list.append("Tonight's recommendation is burbon.")
			drink_list.append('\n')
			drink_list.append(await self.options._get_bourbon())

		if(x == 2):
			drink_list.append("Tonight's recommendation is brandy/cognac.")
			drink_list.append('\n')
			drink_list.append(await self.options._get_brandy())

		if(x == 3):
			drink_list.append("Tonight's recommendation is gin.")
			drink_list.append('\n')
			drink_list.append(await self.options._get_gin())

		if(x == 4):
			drink_list.append("Tonight's recommendation is liqueur.")
			drink_list.append('\n')
			drink_list.append(await self.options._get_liqueur())

		if(x == 5):
			drink_list.append("Tonight's recommendation is a ready to drink concoction.")
			drink_list.append('\n')
			drink_list.append(await self.options._get_r2d())

		if(x == 6):
			drink_list.append("Tonight's recommendation is rum.")
			drink_list.append('\n')
			drink_list.append(await self.options._get_rum())
			
		if(x == 7):
			drink_list.append("Tonight's recommendation is scotch.")
			drink_list.append('\n')
			drink_list.append(await self.options._get_scotch())

		if(x == 8):
			drink_list.append("Tonight's recommendation is tequila.")
			drink_list.append('\n')
			drink_list.append(await self.options._get_tequila())

		if(x == 9):
			drink_list.append("Tonight's recommendation is vodka.")
			drink_list.append('\n')
			drink_list.append(await self.options._get_vodka())

		if(x == 10):
			drink_list.append("Tonight's recommendation is whiskey.")
			drink_list.append('\n')
			drink_list.append(await self.options._get_whiskey())

		await ctx.send(''.join(drink_list))
