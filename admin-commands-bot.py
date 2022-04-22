import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

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
	print("on member update")
	old_nick = before.nick
	print("Old Nick: " + old_nick)

	if old_nick:
		print("new nick being replaced")
		await after.edit(nick="Test Name")
	else:
		await after.edit(nick=None)

@bot.command()
async def randomizeDisplayName(ctx: commands.Context, member:discord.Member):
	# Give Admins the ability to randomize display names
	# await ctx.send("Changing Name for this dude")
	await member.edit(nick="Test Name")


bot.run("#INSERT TOKEN HERE")