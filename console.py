#Citlalmina console v1.0

import sys
import discord
#import abc
#import time
import random
from random import randint
from discord.ext import commands, tasks
#from discord.ext.commands import Bot
#from discord.utils import get
import asyncio
#import datetime as dt
from linereader import copen
#import urllib.request
import time
from datetime import datetime, date
#import pytz
import os
import subprocess

client = discord.Client()

@client.event
async def on_ready():
    os.system("clear")
    intentos = 1
    atte = str(intentos)
    print('\nTehuantin oticpehualticah quen {0.user} ica '.format(client) + atte +
          ' yucateyoliztli.')
    #message_channel = client.get_channel(852785420748324896)
    #await message_channel.send("¡Hola! :3. Gracias por permitirme estar en el servidor, me presento. Soy el inquisidor, en tiempos de antaño fui el bot oficial del clan RAR, pero (si me lo permiten) con gusto puedo ser parte de NwZ :D, ¡Espero que tod@s nos llevemos muy bien! :)")
    print("Status ce oquipehpenalo.")
    print("\nQuitlayecotitica achi tlen " + str(len(client.guilds)) + " tlayecotinimeh.\n")
    await asyncio.sleep(3)
    print("Ximopanolti in Citlalmina Console v1.0")
    await console()

async def console():
  command = input("\n~/Citlalmina$ ")
  if command == "yolmelahualiztin":
    handler = open('yolmelahualiztin.txt')
    ayuda1 = handler.read()
    print("\n" + ayuda1)
    await console()
  elif command == "quipoloa":
    try:
      can = int(input("\nXihihcuilo in canal: "))
      mid = int(input("\nXihihcuilo in amatlacuilolli: "))
      channel = client.get_channel(can)
      mensaje = await channel.fetch_message(mid)
      await mensaje.delete()
      print("\nAmatlacuilolli ihcuilolo")
    except:
      print("\nAhmo ca inon amatlacuilolli nozo canal!")
      await console()
  elif command == "quichipahua":
    os.system("clear")
    await console()
  elif command == "kick":
    try:
      sv = int(input("\nXihihcuilo in tlayecotini: "))
      mid = int(input("\nXihihcuilo in tlacatl: "))
      server = client.get_guild(sv)
      user = await server.fetch_member(mid)
      await server.kick(user, reason=None)
      print("\nTlacatl quizalo")
      await console()
    except:
      print("\nTlacatl nozo tlayecotini ahmo namiquilo!")
      await console()
  elif command == "ban":
    try:
      sv = int(input("\nXihihcuilo in tlayecotini: "))
      mid = int(input("\nXihihcuilo in tlacatl: "))
      server = client.get_guild(sv)
      user = await server.fetch_member(mid)
      await server.ban(user, reason=None)
      print("\nTlacatl quizalo")
      await console()
    except:
      print("\nTlacatl nozo tlayecotini ahmo namiquilo!")
      await console()
  elif command == "lista":
    activeservers = client.guilds
    for guild in activeservers:
        print(guild.name)
    await console()
  elif command == "reboot":
    print("\nQuipehualtitica ayancuipan...")
    await asyncio.sleep(5)
    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
  elif command == "purge":
    try:
      can = int(input("\nXihihcuilo in canal: "))
      n = int(input("\nQuezquintin amatlacuiloltin?: "))
      message_channel = client.get_channel(can)
      await message_channel.purge(limit=n)
      print("\nAmatlacuiloltin poloaloh")
      await console()
    except:
      print("\nCanal ahmo namiquilo!")
      await console()
  elif command == "quititlani":
    try:
      can = int(input("\nXihihcuilo in canal: "))
      message_channel = client.get_channel(can)
      async with message_channel.typing():
        mensaje = input("\nXihihcuilo in amatlacuilolli: ")
        message_channel = client.get_channel(can)
        await message_channel.send(mensaje)
      print("\nAmatlacuilolli titlanilo")
      await console()
    except:
      print("\nCanal ahmo namiquilo!")
      await console()
  elif command == "react":
    try:
      can = int(input("\nXihihcuilo in canal: "))
      mid = int(input("\nXihihcuilo in amatlacuilolli: "))
      rec = input("\nXihihcuilo in reaccion: ")
      channel = client.get_channel(can)
      mensaje = await channel.fetch_message(mid)
      await mensaje.add_reaction(rec)
      print("\nReaccion manalo")
      await console()
    except:
      print("\nAhmo ca inon amatlacuilolli nozo canal nozo reaccion!")
      await console()
  elif command == "ls":
    os.system("ls")
    await console()
  elif command == "quiza":
    sys.exit(0)
  else:
    print("\nComando ahmo namiquilo")
    await console()

client.run('OTEyMTE5NDUxNjk1MDc1MzM4.YZrTbw.7E42zZT2b8AwK_OxeLwpKzACgRY')