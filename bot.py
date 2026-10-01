import os 
import re
from xmlrpc import client
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

GREETING_PATTERN = re.compile(r'\b(hi|hello|hey)\b', re.IGNORECASE)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    content = message.content
    bot_name = bot.user.name

    has_greeting = GREETING_PATTERN.search(content)
    has_bot_name = re.search(rf'\b{re.escape(bot_name)}\b', content, re.IGNORECASE)

    if has_greeting and has_bot_name:
        await message.channel.send(f'Hello {message.author.name}! 👋. What can i do for you?')

    await bot.process_commands(message)

@bot.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user.mention} added a reaction to {reaction.message.author.mention}\'s message!')


bot.run(TOKEN)




