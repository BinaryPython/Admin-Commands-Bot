import discord
import asyncio
from discord.ext import commands
import logging
# from pprint import pprint

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
		penalty_data = member_penalties[before.id]

		if penalty_data[0] == "name_change" and after.nick != penalty_data[1]:
			await after.edit(nick=penalty_data[1])


@bot.command()
async def randomName(ctx: commands.Context, member:discord.Member):
	# Give Admins the ability to randomize display names
	# await ctx.send("Changing Name for this dude")

	newName = "New Name"
	member_penalties[member.id] = ("name_change",newName)

	await member.edit(nick=newName)


bot.run("#INSERT TOKEN HERE")