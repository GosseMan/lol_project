import discord
from discord.ext import commands
from to import Token

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')

@bot.command()
async def hello(message):
    await message.channel.send('Hi!')

bot.run(Token)