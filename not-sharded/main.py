#import everything needed
import discord
from discord.ext import commands

#change the content of "" to what you want your prefix to be
bot=commands.Bot(command_prefix="!")

#Here's an example of a command
@bot.command()
async def ping(ctx):
  await ctx.send("Pong!")

#Here's an example of an event
@bot.event
async def on_ready():
  print(f"Logged in as {bot.user}")
  
#replace TOKEN with your bot token
bot.run("TOKEN")
