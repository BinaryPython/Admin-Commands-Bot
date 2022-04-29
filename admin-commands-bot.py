import discord
import asyncio
from discord.ext import commands
import logging
import random
import datetime

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.members = True

member_penalties = {}

bot = commands.Bot(command_prefix=commands.when_mentioned,intents=intents)

@bot.event
async def on_ready():
	print("Bot is logged in")
	print("----------------")


@bot.event
async def on_disconnect():
	print("-------------------------")
	print("Bot has been Disconnected")
	print("-------------------------")


@bot.event
async def on_member_update(before,after):
	if before.id in member_penalties.keys():
		penalty_name, penalty_time, penalty_data= member_penalties[before.id]

		curTime = datetime.datetime.utcnow()

		if curTime > penalty_time:
			del member_penalties[before.id]
			return False

		if (penalty_name == "name_change" and 
				after.nick != penalty_data):
			await after.edit(nick=penalty_data)


@bot.command()
async def randomName(ctx: commands.Context, member:discord.Member, time=None):
	# Give Admins the ability to randomize display names
	# await ctx.send("Changing Name for this dude")

	if ctx.author.guild_permissions.administrator == False:
		await ctx.send("You don't have permissions to use this command.")
		return False

	names = [
		"Some Nerd",
		"Ya Boi",
		"The Imposter",
		"The 'Alpha' (Not Really)",
		"Zesty Zebra",
		"Mr.President",
		"The Modern Rebel Girl",
		"BoomBlaster",
		"Goofy Girl",
		"The Zodiac Killer",
		"Mustard Gas",
		"Knuckle Breaker",
		"Osama's Ghost",
		"Hakuna Matata",
		"Very Sus",
		"Greedy Scrapper",
		"Jaded Troll",
		"Bony Castaway",
		"No Fun 4 You",
		"DownInSmoke",
		"Crash Override",
		"Bitten by a Zombie",
		"Fuzzy Pack",
		"Confused Troll",
		"Cavern Troll",
		"A Leper",
		"Brash Thug",
		"Amusing Gangster",
		"Loser of the Seven Seas",
		"Grog Lover",
		"Gloomy Shaman",
		"Noxious Wretch",
		"Mudbrew Degenerate",
		"Reckless Assailant",
		"Marsh Brawler",
		"Haunting Brute",
		"Hillforce Slugger",
		"Defiant Wretch",
		"Toadstool Barbarian",
		"Defiant Vagabond",
		"Gloomy Wretch",
		"A Horny Simp",
		"Blind Brawler"
	]

	#if time == None:
	revertTime = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
	# else:
	# 	revertTime = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)

	newName = random.choice(names)

	member_penalties[member.id] = ("name_change",revertTime,newName)
	await member.edit(nick=newName)

	await ctx.send("The name change was completed and will last for 5 minutes")


bot.run("#INSERT TOKEN HERE")