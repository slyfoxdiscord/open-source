#This is where we import things
import discord
from discord.ext import commands

#replace the content of the "" with the prefix you desire
#also replace the number of shards with how many shards you desire
bot=commands.AutoShardedBot(command_prefix="!", shard_count=2)

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
