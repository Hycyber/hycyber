# activate Birb

import discord
import random

from redbot.core import commands
from random import randrange

class Birb(commands.Cog):
	"""Conglomerate of requested commands. To be seperated into cogs later"""
	
# Oosmus's requested commands	
     #!screm	
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
     #!aaa		
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
     #!babe
	@commands.Cog.listener()
	async def on_message(self, message):
		listenWords = ["babe", "babe.", "babe?", "babe!", "bab3", "dawg"]
		urls = ["https://i.pinimg.com/control/236x/09/1d/cf/091dcfc270ebfd903764d97dce90a053.jpg",
			"https://i.pinimg.com/control/236x/3b/a7/b7/3ba7b76c1c9bceea00a391be56a1b7b9.jpg",
			"https://i.pinimg.com/control/474x/d1/3f/1e/d13f1e43a25162f2b64822dd3dff4d9e.jpg",
			"https://i.pinimg.com/control/236x/9d/db/2a/9ddb2a53f2bc562c4dd18fea7279ab31.jpg",
			"https://i.pinimg.com/control/474x/80/ce/eb/80ceebe64c2d4c65be0a85127eb8e2c1.jpg",
			"https://i.pinimg.com/control/474x/88/ca/66/88ca6644cccebcf106672e9560bea131.jpg",
			"https://i.pinimg.com/control/474x/b6/f8/fb/b6f8fbbf49c9bd0ed4f5827e639a3a33.jpg",
			"https://i.pinimg.com/474x/e8/2d/75/e82d75656dab1033f17da464cd2728a5.jpg",
			"https://i.pinimg.com/236x/ce/f4/03/cef403deba3128aa385710989e32b3e9.jpg",
			"https://i.pinimg.com/control/236x/e8/10/e0/e810e0b17fc9fdb827c3272bdcda4320.jpg",
			"https://i.pinimg.com/control/236x/ed/e6/54/ede654ba4e507759e994185083b344b7.jpg",
			"https://i.pinimg.com/control/236x/3e/08/f5/3e08f54028143bc68ad0e8c883a75e42.jpg"
		       ]
		msg = message.content.lower()
		if any(word in msg for word in listenWords):
			await message.channel.send(random.choice(urls))
			await bot.process_commands(message)
		else:
			return
     #!becky			
	@commands.command()
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
		x = randrange(1,5)

		for num in range(0,x):
			y = randrange(0,2) 
			if y > 0:
				becky_list.append(random.choice(becky))
				becky_list.append('\n')
			else:
				becky_list.append('stik')
				becky_list.append('\n')

		await ctx.send(''.join(becky_list))
     #!ron
	@commands.command()
	async def ron(self, ctx):
		"""ron quotes"""
		ron_list =[]
		ron =  ["Lemme smash",
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
		x = randrange(1,15)

		for num in range(0,x):
			y = randrange(0,2)
			if y > 0:
				ron_list.append(random.choice(ron))
				ron_list.append('\n')
			else:
				ron_list.append('stik')
				ron_list.append('\n')

		await ctx.send(''.join(ron_list))
		
		
     #!dook		
	@commands.command()
	async def dook(self, ctx):
		"""Command requested by Kira"""
		dook_list = []
		num = 0
		x = randrange(1,20)

		for num in range(0,x):
			dook_list.append("dook  ")
		await ctx.send(''.join(dook_list))
		
     #!fack
	@commands.command()
	async def fack(self, ctx):
		await ctx.send("https://tenor.com/view/fuckthat-fuckthis-fuckeverything-fuck-ferret-gif-4531930")
		
# End Oosmus's requested commands
# Plague's requested commands
     #!boomer
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
# End Plague's requested commands

# Rabbit's requested commands
     #!groovy
	@commands.command()
	async def groovy(self, ctx):
		"""groovy command requested by rabbit"""
		groovy = []
		num = 0
		x = randrange(2,200)
		
		groovy.append("That's Gr")

		for num in range(0,x):
			y = randrange(0,2)
			if(y > 0):
				groovy.append("O")
			else:
				groovy.append("o")
		groovy.append("vy, dude")
		await ctx.send(''.join(groovy))
     #!soundthealarm		
	@commands.command()
	async def soundthealarm(self, ctx):
		"""Command requested by rabbit"""
		thump_list = []
		num = 0
		x = randrange(1,20)

		for num in range(0,x):
			thump_list.append("THUMP ")
		await ctx.send(''.join(thump_list))
     #!tea		
	@commands.command()
	async def tea(self, ctx):
		"""Command requested by rabbit"""
		tea_list =[]
		tea = [  "give me the tea",
			 "give it now",
			 "give give give",
			 "so thirsty",
			 "I ordered tea, where is it?",
			 "Where is it?",
			 "Tea? Tea?",
			 "Tea give life.",
			 "RAB-BOT demands tea!"]
        
		num = 0
		x = randrange(1,5)

		for num in range(0,x):
			tea_list.append(random.choice(tea))
			tea_list.append('\n')

		await ctx.send(''.join(tea_list))
      #!pog
	@commands.command()
	async def pog(self, ctx):
		await ctx.send("https://tenor.com/view/monkey-pog-pog-poggers-monke-pog-monkey-poggers-gif-19560507")

     #!libertymedical
	@commands.command()
	async def libertymedical(self, ctx):
		await ctx.send("https://tenor.com/view/diabetes-diabeetus-cat-angry-cat-mad-cat-gif-5935791")

# End rabbit's requested commands
# Start Hycyber's designed commands
     #!fish
	@commands.command()
	async def fish(self, ctx):
		await ctx.send("https://tenor.com/view/pog-pogfish-fish-openmouth-gif-20357594")
		
    #!poyo
	@commands.command()
	async def poyo(self, ctx):
		poyo = [ "https://i.kym-cdn.com/photos/images/original/001/685/114/d71.gif",
			"https://www.icegif.com/wp-content/uploads/icegif-59.gif",
			"https://media1.tenor.com/images/5d7b75d021b607d13486ef63549431e3/tenor.gif?itemid=18598276",
			"https://media.tenor.com/images/b1606545de66e06520f5699b88489bf6/tenor.gif",
			"https://i.imgflip.com/56ijju.gif",
			"https://media.tenor.com/images/4bad4c2a4b36b39e14d1e79db2d510ef/tenor.gif",
			"https://media.tenor.com/images/d16e73591ecf6409eefd295f49901d3d/tenor.gif",
		        "https://media.giphy.com/media/V8GXG0bDve5GLs1K0v/giphy.gif"]
		await ctx.send(random.choice(poyo))
		
#End Hycyber's designed commands
#Start Jebby's designed commands
     #!jebby
	@commands.command()
	async def jebby(self, ctx):
		await ctx.message.delete()
		await ctx.send("https://i.imgur.com/V3QNiU1.jpeg")
			
#End Jebby's designed commands
	def cog_unload(self):
		self.bot.loop.create_task(self.session.close())

	__del__ = cog_unload
