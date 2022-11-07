import nextcord
from nextcord.ext import commands
import discord
import os
import requests, json, random, datetime, asyncio

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name="hi")
async def SendMessage(ctx):
  await ctx.send('Hi!')

async def schedule_daily_message():
  now = datetime.datetime.now()
  #then = now+datetime.timedelta(days=1)
  then = now.replace(hour=16, minute=22)
  wait_time = (then-now).total_seconds()
  await asyncio.sleep(wait_time)

  channel = bot.get_channel(721320073272229961)

  await channel.send("Good morning!!")

@bot.event
async def on_ready():
  print(f'We have logged in as: {bot.user.name}')
  await schedule_daily_message()

if __name__ == '__main__':
  bot.run(os.environ["DISCORD_TOKEN"])