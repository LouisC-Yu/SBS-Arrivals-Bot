import discord
from discord.ext import commands
import sbsscraper

f = open('.gitignore.txt', 'r')
TOKEN = f.read()
f.close()

bot = commands.Bot(command_prefix = '!b ', case_insensitive = True)

@bot.event
async def on_ready():
    print("Bot ready")

@bot.listen()
async def on_message(message):
    message.content = message.content.lower()
    if message.author == bot.user:
        return
    if message.content.startswith("beep"):
        msg = '{0.author.mention} boop'.format(message)
        await message.channel.send(msg)

@bot.command(name = 'ping')
async def ping(ctx):
    ping = round(bot.latency *1000)
    await ctx.send(f'{ping}ms')

@bot.command()
async def arrive(ctx, station, service=None):
    station = str(station)
    if service is None:
        msg = sbsscraper.all_service(station)
        await ctx.send(msg)
    else:
        service = str(service)
        msg = sbsscraper.a_service(station, service)
        await ctx.send(msg)

bot.run(TOKEN)
