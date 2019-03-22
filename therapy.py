import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import feedparser
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


bot = ChatBot(
	'Rachel',
	storage_adapter='chatterbot.storage.SQLStorageAdapter',
	database_uri='sqlite:///database.sqlite3'
)

trainer = ListTrainer(bot)

trainer.train([
	'How are you?',
	'I am good.',
	'That is good to hear.',
	'Thank you',
	'You are welcome.',
])



client = Bot(description="cbt bot by Kat", command_prefix="", pm_help = False)


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
	if message.content.startswith('Rachel') or message.content.startswith('rachel') or message.content.startswith('rach'):
		await client.send_message(message.channel, 'Hello')
		msg = await client.wait_for_message(author=message.author)
		response = chatbot.get_response('I would like to book a flight.')
		await client.send_message(message.channel, response)

client.run('')

