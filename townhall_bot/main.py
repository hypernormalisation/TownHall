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


test_embed = discord.Embed(
    title='Townhall',
    url='https://github.com/hypernormalisation/TownHall',
    description="Townhall is a Discord bot to handle your realm's guild organisation needs.",
    color=discord.Color.red()
)

bot = discord.Bot()


@bot.slash_command()
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello {name}!")


@bot.user_command(name="Say Hello")
async def hi(ctx, user):
    await ctx.respond(f"{ctx.author.mention} says hello to {user.name}!")

bot.run(my_bot_token)
