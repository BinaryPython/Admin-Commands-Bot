import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned)

@bot.command()
async def randomizeDisplayName(ctx: commands.Context):
	# Give Admins the ability to randomize display names
	pass


bot.run("#INSERT TOKEN HERE")