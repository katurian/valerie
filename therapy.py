import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import feedparser


client = Bot(description="cbt bot by Kat", command_prefix="!", pm_help = False)

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Made by Kate Kulinski')
	return await client.change_presence(game=discord.Game(name='Reading!'))

@client.event
async def on_message(message):
    if message.content.startswith('$'):
      print("kate")

client.run('')
