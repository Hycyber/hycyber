# activate Birb

import discord
import random

from redbot.core import commands
from random import randrange

BaseCog = getattr(commands, "Cog", object)

class Birb(BaseCog):
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

# End rabbit's requested commands
# Start Hycyber's designed commands
     #!fish
	@commands.command()
	async def fish(self, ctx):
		await ctx.send("https://tenor.com/view/pog-fish-fish-mouth-open-gif-17487624")
		
 #!drink
	@commands.command()
	async def drink(self, ctx):
		await ctx.send("!play https://www.youtube.com/watch?v=f55CqLc6IR0")
		
     #!liqa
	@commands.command()
	async def liqa(self, ctx):
		"""tells you what to get from the store"""
		drink_list =[]
		drink_list.append("Currently in beta, more choices to come later")
		drink_list.append('\n')
		bourbon =  ["RUSSELL'S RESERVE 6YR RYE: https://www.totalwine.com/spirits/bourbon/small-batch-bourbon/russells-reserve-6yr-rye/p/46841750?s=801&igrules=true",
			"JIM BEAM SINGLE BARREL 108 PROOF: https://www.totalwine.com/spirits/bourbon/small-batch-bourbon/jim-beam-single-barrel-108-proof/p/224249750?s=801&igrules=true",
			"VIRGIL KAINE GINGER INFUSED BOURBON: https://www.totalwine.com/spirits/bourbon/virgil-kaine-ginger-infused-bourbon/p/121349750?s=801&igrules=true",
			"BIRD DOG KENTUCKY STRAIGHT BOURBON 84 PROOF: https://www.totalwine.com/spirits/bourbon/small-batch-bourbon/bird-dog-kentucky-straight-bourbon-84-proof/p/231881750?s=801&igrules=true",
			"ASW FIDDLER UNISON BOURBON: https://www.totalwine.com/spirits/bourbon/asw-fiddler-unison-bourbon/p/190755750?s=801&igrules=true",
			"HIRSCH HORIZON BOURBON: https://www.totalwine.com/spirits/bourbon/small-batch-bourbon/hirsch-horizon-bourbon/p/230979750?s=801&igrules=true",
			"VERY OLD BARTON 90 PF: https://www.totalwine.com/spirits/bourbon/very-old-barton-90-pf/p/169772175?s=801&igrules=true",
			"REDWOOD EMPIRE PIPE DREAM WHISKEY: https://www.totalwine.com/spirits/bourbon/redwood-empire-pipe-dream-whiskey/p/184407750?s=801&igrules=true",
			"PINHOOK FLAGSHIP BOURBON WHISKEY: https://www.totalwine.com/spirits/bourbon/small-batch-bourbon/pinhook-flagship-bourbon-whiskey/p/232301750?s=801&igrules=true",
			"JACK DANIELS LEGACY EDITION 2: https://www.totalwine.com/spirits/bourbon/jack-daniels-legacy-edition-2/p/191358750?s=801&igrules=true"]
		brandy = ["ABK6 VSOP COGNAC: https://www.totalwine.com/spirits/brandy-cognac/cognac/abk6-vsop-cognac/p/135127750?s=801&igrules=true",
			"1889 ROYAL BRANDY: https://www.totalwine.com/spirits/brandy-cognac/brandy/1889-royal-brandy/p/171047175?s=801&igrules=true",
			"E & J BRANDY: https://www.totalwine.com/spirits/brandy-cognac/brandy/e-j-brandy/p/1007175?s=801&igrules=true",
			"KORBEL BRANDY: https://www.totalwine.com/spirits/brandy-cognac/brandy/korbel-brandy/p/5736175?s=801&igrules=true",
			"FIDELITAS KIRSCHWASSER: https://www.totalwine.com/spirits/brandy-cognac/eau-de-vie/fidelitas-kirschwasser/p/115921750?s=801&igrules=true",
			"CHATEAU DE LAUBADE SIGNATURE ARMAGNAC: https://www.totalwine.com/spirits/brandy-cognac/armagnac/chateau-de-laubade-signature-armagnac/p/117663750?s=801&igrules=true",
			"MAURO SEBASTE MOSCATO GRAPPA: https://github.com/Hycyber/hycyber/edit/main/birb/birb.py",
			"BANKERS CLUB BRANDY: https://www.totalwine.com/spirits/brandy-cognac/brandy/bankers-club-brandy/p/7587175?s=801&igrules=true",
			"CHATEAU DE LACQUY REFERENCE: https://www.totalwine.com/spirits/brandy-cognac/armagnac/chateau-de-lacquy-reference/p/226866750?s=801&igrules=true",
			"D'USSE COGNAC VSOP: https://www.totalwine.com/spirits/brandy-cognac/cognac/dusse-cognac-vsop/p/130477375?s=801&igrules=true"]
		
		x = randrange(1,2)
		
		if(x == 1):
			drink_list.append("Tonight's choice is burbon: ")
			drink_list.append('\n')
			drink_list.append(random.choice(burbon))
			
		if(x == 2):
			drink_list.append("Tonight's choice is brandy/cognac: ")
			drink_list.append('\n')
			drink_list.append(random.choice(brandy))
		
	
		await ctx.send(''.join(drink_list))
		
#End Hycyber's designed commands
	def cog_unload(self):
		self.bot.loop.create_task(self.session.close())

	__del__ = cog_unload
