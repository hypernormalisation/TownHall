"""TownHall Discord Bot

This program implements a Discord bot for the management of WoW guilds
on a realm discord.

"""
import discord
import os
import sys
from dotenv import load_dotenv

# Load the bot token from the .env file.
load_dotenv()
my_bot_token = os.environ.get('bot_token')

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(my_bot_token)
