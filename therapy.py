import os
import sys

import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import argparse
from collections import deque

from cakechat.utils.env import init_theano_env

init_theano_env()

from cakechat.api.response import get_response
from cakechat.config import INPUT_CONTEXT_SIZE, DEFAULT_CONDITION
from cakechat.utils.telegram_bot_client import TelegramBot, AbstractTelegramChatSession


client = Bot(description="cbt bot by Kat", command_prefix="!", pm_help = False)


@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Made by Kate Kulinski')
	return await client.change_presence(game=discord.Game(name='Barbie Horse Adventures'))

@client.event
async def on_message(message):
	if (message.author.bot == True):
		return
	if message.content.startswith('-'):
		msg = [str(message.content)[1:]]
		response = get_response(msg, DEFAULT_CONDITION)
		await client.send_message(message.channel, response)

client.run('CLIENT-TOKEN')
