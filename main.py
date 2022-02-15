#Citlalmina, bot para Discord hecho por Tonantzin Flores, v5.8

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
import requests
from bs4 import BeautifulSoup
#import urllib.request
import asyncpraw
import time
from datetime import datetime, date
#import pytz
from googletrans import Translator
import pafy
from pafy import new
from discord.voice_client import VoiceClient
import nacl
import ffmpeg
from discord import FFmpegPCMAudio
from hijri_converter import convert
import pytz
import sys
import subprocess
import os
import youtube_dl

translator = Translator()
client = discord.Client()
reddit = asyncpraw.Reddit(client_id='KKUbusrGxqLq5aXGDsD0Ew',
                  client_secret='RWAahteZ0VvNHY-2oFebu_GdZidECw',
                  user_agent='thelvadam-memes')
listavote=[]
reacciones=[]
contador = 1
loops = False
pi = 0

LANGUAGES = {
    'af': 'Afrikaans',
    'sq': 'Albanian',
    'am': 'Amharic',
    'ar': 'Arabic',
    'hy': 'Armenian',
    'az': 'Azerbaijani',
    'eu': 'Basque',
    'be': 'Belarusian',
    'bn': 'Bengali',
    'bs': 'Bosnian',
    'bg': 'Bulgarian',
    'ca': 'Catalan',
    'ceb': 'Cebuano',
    'ny': 'Chichewa',
    'zh-cn': 'Chinese (simplified)',
    'zh-tw': 'Chinese (traditional)',
    'co': 'Corsican',
    'hr': 'Croatian',
    'cs': 'Czech',
    'da': 'Danish',
    'nl': 'Dutch',
    'en': 'English',
    'eo': 'Esperanto',
    'et': 'Estonian',
    'tl': 'Filipino',
    'fi': 'Finnish',
    'fr': 'French',
    'fy': 'Frisian',
    'gl': 'Galician',
    'ka': 'Georgian',
    'de': 'German',
    'el': 'Greek',
    'gu': 'Gujarati',
    'ht': 'Haitian creole',
    'ha': 'Hausa',
    'haw': 'Hawaiian',
    'iw': 'Hebrew',
    'he': 'Hebrew',
    'hi': 'Hindi',
    'hmn': 'Hmong',
    'hu': 'Hungarian',
    'is': 'Icelandic',
    'ig': 'Igbo',
    'id': 'Indonesian',
    'ga': 'Irish',
    'it': 'Italian',
    'ja': 'Japanese',
    'jw': 'Javanese',
    'kn': 'Kannada',
    'kk': 'Kazakh',
    'km': 'Khmer',
    'ko': 'Korean',
    'ku': 'Kurdish (kurmanji)',
    'ky': 'Kyrgyz',
    'lo': 'Lao',
    'la': 'Latin',
    'lv': 'Latvian',
    'lt': 'Lithuanian',
    'lb': 'Luxembourgish',
    'mk': 'Macedonian',
    'mg': 'Malagasy',
    'ms': 'Malay',
    'ml': 'Malayalam',
    'mt': 'Maltese',
    'mi': 'Maori',
    'mr': 'Marathi',
    'mn': 'Mongolian',
    'my': 'Myanmar (burmese)',
    'ne': 'Nepali',
    'no': 'Norwegian',
    'or': 'Odia',
    'ps': 'Pashto',
    'fa': 'Persian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'pa': 'Punjabi',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sm': 'Samoan',
    'gd': 'Scots gaelic',
    'sr': 'Serbian',
    'st': 'Sesotho',
    'sn': 'Shona',
    'sd': 'Sindhi',
    'si': 'Sinhala',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'so': 'Somali',
    'es': 'Spanish',
    'su': 'Sundanese',
    'sw': 'Swahili',
    'sv': 'Swedish',
    'tg': 'Tajik',
    'ta': 'Tamil',
    'te': 'Telugu',
    'th': 'Thai',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'ug': 'Uyghur',
    'uz': 'Uzbek',
    'vi': 'Vietnamese',
    'cy': 'Welsh',
    'xh': 'Xhosa',
    'yi': 'Yiddish',
    'yo': 'Yoruba',
    'zu': 'Zulu'
    }

idiomasx = {
    'af': 'Afrikáans',
    'sq': 'Albanés',
    'am': 'Amhárico',
    'ar': 'Árabe',
    'hy': 'Armenio',
    'az': 'Azerí',
    'eu': 'Vasco',
    'be': 'Bielorruso',
    'bn': 'Bengalí',
    'bs': 'Bosnio',
    'bg': 'Búlgaro',
    'ca': 'Catalán',
    'ceb': 'Cebuano',
    'ny': 'Chichewa',
    'zh-cn': 'Chino (simplificado)',
    'zh-tw': 'Chino (tradicional)',
    'co': 'Corso',
    'hr': 'Croata',
    'cs': 'Checo',
    'da': 'Danés',
    'nl': 'Neerlandés',
    'en': 'Inglés',
    'eo': 'Esperanto',
    'et': 'Estonio',
    'tl': 'Filipino',
    'fi': 'Finés',
    'fr': 'Francés',
    'fy': 'Frisio',
    'gl': 'Gaélico',
    'ka': 'Georgiano',
    'de': 'Alemán',
    'el': 'Griego',
    'gu': 'Gujaratí',
    'ht': 'Criollo haitiano',
    'ha': 'Hausa',
    'haw': 'Hawaiano',
    'iw': 'Hebreo',
    'he': 'Hebreo',
    'hi': 'Hindi',
    'hmn': 'Hmong',
    'hu': 'Húngaro',
    'is': 'Islandés',
    'ig': 'Igbo',
    'id': 'Indonesio',
    'ga': 'Irlandés',
    'it': 'Italiano',
    'ja': 'Japonés',
    'jw': 'Javanés',
    'kn': 'Canarés',
    'kk': 'Kazajo',
    'km': 'Khmer',
    'ko': 'Coreano',
    'ku': 'Kurdo (kurmanji)',
    'ky': 'Kyrgyz',
    'lo': 'Lao',
    'la': 'Latín',
    'lv': 'Letón',
    'lt': 'Lituano',
    'lb': 'Luxemburgués',
    'mk': 'Macedonio',
    'mg': 'Malgache',
    'ms': 'Malayo',
    'ml': 'Malayalam',
    'mt': 'Maltés',
    'mi': 'Maorí',
    'mr': 'Marathi',
    'mn': 'Mongol',
    'my': 'Myanmar',
    'ne': 'Nepalí',
    'no': 'Noruego',
    'or': 'Odia',
    'ps': 'Pashto',
    'fa': 'Persa',
    'pl': 'Polaco',
    'pt': 'Portugués',
    'pa': 'Punjabi',
    'ro': 'Rumano',
    'ru': 'Ruso',
    'sm': 'Samoa',
    'gd': 'Gaelico escocés',
    'sr': 'Serbio',
    'st': 'Sesotho',
    'sn': 'Shona',
    'sd': 'Sindhi',
    'si': 'Sinhala',
    'sk': 'Eslovaco',
    'sl': 'Esloveno',
    'so': 'Somalí',
    'es': 'Español',
    'su': 'Sundanés',
    'sw': 'Swahili',
    'sv': 'Sueco',
    'tg': 'Tajik',
    'ta': 'Tamil',
    'te': 'Telugu',
    'th': 'Tailandés',
    'tr': 'Turco',
    'uk': 'Ucraniano',
    'ur': 'Urdu',
    'ug': 'Uigur',
    'uz': 'Uzbeco',
    'vi': 'Vietnamita',
    'cy': 'Welsh',
    'xh': 'Xhosa',
    'yi': 'Yiddish',
    'yo': 'Yoruba',
    'zu': 'Zulu'}

@client.event
async def on_ready():
    intentos = 1
    atte = str(intentos)
    print('\nTehuantin oticpehualticah quen {0.user} ica '.format(client) + atte +
          ' yucateyoliztli.')
    #message_channel = client.get_channel(852785420748324896)
    #await message_channel.send("¡Hola! :3. Gracias por permitirme estar en el servidor, me presento. Soy el inquisidor, en tiempos de antaño fui el bot oficial del clan RAR, pero (si me lo permiten) con gusto puedo ser parte de NwZ :D, ¡Espero que tod@s nos llevemos muy bien! :)")
    print("Status ce oquipehpenalo.")
    print("\nQuitlayecotitica achi tlen " + str(len(client.guilds)) + " tlayecotinimeh.\n")
    while True:
      await set_date()
      await asyncio.sleep(1800)

async def set_date():
  dt_us_central = datetime.now(pytz.timezone('America/Mexico_City'))
  año = int(dt_us_central.strftime("%Y"))
  if año == 2021:
    xihuitl = "9 Calli"
  elif año == 2022:
    xihuitl = "10 Tochtli"
  elif año == 2023:
    xihuitl = "11 Acatl"
  elif año == 2024:
    xihuitl = "12 Tecpatl"
  elif año == 2025:
    xihuitl = "13 Calli"
  fecha = float(dt_us_central.strftime("%m.%d"))
  dia = int(dt_us_central.strftime("%d"))
  if 02.02 <= fecha <= 02.21:
    dia2 = str(dia - 1)
    tonalli = dia2 + " Atlachualo"
  elif 02.22 <= fecha <= 03.13:
    if fecha <= 02.28:
      dia2 = str(dia - 21)
      tonalli = dia2 + " Tlacaxipehualiztli"
    else:
      dia2 = str(dia + 28 - 21)
      tonalli = dia2 + " Tlacaxipehualiztli"
  elif 03.14 <= fecha <= 04.02:
    if fecha <= 03.31:
      dia2 = str(dia - 13)
      tonalli = dia2 + " Tzoztontli"
    else:
      dia2 = str(dia + 31 - 13)
      tonalli = dia2 + " Tzoztontli"
  elif 04.03 <= fecha <= 04.22:
    dia2 = str(dia - 2)
    tonalli = dia2 + " Huey Tzoztli" 
  elif 04.23 <= fecha <= 05.12:
    if fecha <= 04.30:
      dia2 = str(dia - 22)
      tonalli = dia2 + " Toxcatl"
    else:
      dia2 = str(dia + 30 - 22)
      tonalli = dia2 + " Toxcatl"  
  elif 05.13 <= fecha <= 06.01:
    if fecha <= 05.31:
      dia2 = str(dia - 12)
      tonalli = dia2 + " Etzalcualiztli"
    else:
      dia2 = str(dia + 31 - 12)
      tonalli = dia2 + " Etzalcualiztli"
  elif 06.02 <= fecha <= 06.21:
    dia2 = str(dia - 2)
    tonalli = dia2 + " Tecuilhuitontli"
  elif 06.22 <= fecha <= 07.11:
    if fecha <= 06.30:
      dia2 = str(dia - 21)
      tonalli = dia2 + " Huey Tecuilhuitl"
    else:
      dia2 = str(dia + 30 - 21)
      tonalli = dia2 + " Huey Tecuilhuitl"
  elif 07.12 <= fecha <= 07.31:
    dia2 = str(dia - 11)
    tonalli = dia2 + " Miccailhuitontli"
  elif 08.01 <= fecha <= 08.20:
    tonalli = dia + " Huey Miccailhuitl"
  elif 08.21 <= fecha <= 09.09:
    if fecha <= 08.31:
      dia2 = str(dia - 20)
      tonalli = dia2 + " Ochpaniztli"
    else:
      dia2 = str(dia + 31 - 20)
      tonalli = dia2 + " Ochpaniztli"
  elif 09.10 <= fecha <= 09.29:
    dia2 = str(dia - 9)
    tonalli = dia2 + " Teotlehco"
  elif 09.30 <= fecha <= 10.19:
    if fecha <= 09.30:
      dia2 = str(dia - 29)
      tonalli = dia2 + " Tepeilhuitl"
    else:
      dia2 = str(dia + 30 - 29)
      tonalli = dia2 + " Tepeilhuitl"
  elif 10.20 <= fecha <= 11.08:
    if fecha <= 10.31:
      dia2 = str(dia - 19)
      tonalli = dia2 + " Quecholli"
    else:
      dia2 = str(dia + 31 - 19)
      tonalli = dia2 + " Quecholli"
  elif 11.09 <= fecha <= 11.28:
    dia2 = str(dia - 8)
    tonalli = dia2 + " Panquetzaliztli"
  elif 11.29 <= fecha <= 12.18:
    if fecha <= 11.39:
      dia2 = str(dia - 28)
      tonalli = dia2 + " Atemoztli"
    else:
      dia2 = str(dia + 30 - 28)
      tonalli = dia2 + " Atemoztli"
  elif 12.19 <= fecha <= 12.31:
    dia2 = str(dia - 18)
    tonalli = dia2 + " Tititl"
  elif 01.01 <= fecha <= 01.07:
    dia2 = str(dia + 31 - 18)
    tonalli = dia2 + " Tititl"
  elif 01.08 <= fecha <= 01.27:
    dia2 = str(dia - 7)
    tonalli = dia2 + " Izcalli"
  elif 01.28 <= fecha <= 02.01:
    if fecha <= 01.31:
      dia2 = str(dia - 27)
      tonalli = dia2 + " Nemontemi"
    else:
      dia2 = str(dia + 31 - 27)
      tonalli = dia2 + " Nemontemi"

  await client.change_presence(activity=discord.Game(name="Fin de soporte técnico 2021.12.21"))

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    mensaje1 = message.content
    global loops
    global author
    global channel
    global voice
    global pi
    global playlistvideo
    global playlistdesc

    """if "jueputa" in listamensaje:
        await strikes(message)
        await groserias(message)
    elif "hijueputa" in listamensaje:
        await strikes(message)
        nombre1 = str(message.author.id)
        await groserias(message)
    elif "gonorrea" in listamensaje:
        await strikes(message)
        nombre1 = str(message.author.id)
        await groserias(message)
    elif "malparida" in listamensaje:
        await strikes(message)
        nombre1 = str(message.author.id)
        await groserias(message)
    elif "malparido" in listamensaje:
        await strikes(message)
        nombre1 = str(message.author.id)
        await groserias(message)
    elif "Jueputa" in listamensaje:
        await strikes(message)
        nombre1 = str(message.author.id)
        await groserias(message)
    elif "Hijueputa" in listamensaje:
        await strikes(message)
        nombre1 = str(message.author.id)
        await groserias(message)
    elif "ijueputa" in listamensaje:
        await strikes(message)
        nombre1 = str(message.author.id)
        await groserias(message)
    elif "Ijueputa" in listamensaje:
        await strikes(message)
        nombre1 = str(message.author.id)
        await groserias(message)
    elif "Malparido" in listamensaje:
        await strikes(message)
        nombre1 = str(message.author.id)
        await groserias(message)
    elif "Malparida" in listamensaje:
        await strikes(message)
        nombre1 = str(message.author.id)
        await groserias(message)
    elif "Gonorrea" in listamensaje:
        await strikes(message)
        nombre1 = str(message.author.id)
        await groserias(message)
    elif "puto" in listamensaje:
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!721920162005123142>":
            return
        else:
            await groserias(message)
    elif "Puto" in listamensaje:
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!721920162005123142>":
            return
        else:
            await groserias(message)
    elif "puta" in listamensaje:
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!721920162005123142>":
            return
        else:
            await strikes(message)
            await groserias(message)
    elif "Puta" in listamensaje:
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!721920162005123142>":
            return
        else:
            await strikes(message)
            await groserias(message)
    elif "hijo de p" in listamensaje:
        await strikes(message)
        await groserias(message)
    elif "Hijo de p" in listamensaje:
        await strikes(message)
        await groserias(message)
    elif "hdp" in listamensaje:
        await strikes(message)
        await groserias(message)
    elif "HDP" in listamensaje:
        await strikes(message)
        await groserias(message)
    elif "Hija de p" in listamensaje:
        await strikes(message)
        await groserias(message)
    elif "hija de p" in listamensaje:
        await strikes(message)
        await groserias(message)
    elif "fuck" in listamensaje:
        await groserias(message)
    elif "Fuck" in listamensaje:
        await groserias(message)
    if "bullshit" in listamensaje:
        await strikes(message)
        await groserias(message)
    elif "Bullshit" in listamensaje:
        await strikes(message)
        await groserias(message)
    elif "bitch" in listamensaje:
        await strikes(message)
        await groserias(message)
    elif "Bitch" in listamensaje:
        await strikes(message)
        await groserias(message)
    elif "bitch?" in listamensaje:
        await strikes(message)
        await groserias(message)
    elif "Bitch?" in listamensaje:
        await strikes(message)
        await groserias(message)
    elif "perra" in listamensaje:
        await strikes(message)
        await groserias(message)
    elif "perro" in listamensaje:
        await groserias(message)
    elif "Perra" in listamensaje:
        await groserias(message)
    elif "Perro" in listamensaje:
        await groserias(message)
    elif "prra" in listamensaje:
        await groserias(message)
    elif "prro" in listamensaje:
        await groserias(message)
    elif "Prra" in listamensaje:
        await groserias(message)
    elif "Prro" in listamensaje:
        await groserias(message)

    if ":regional_indicator_h:ijueputa" in listamensaje:
        await strikes(message)
        await groserias(message)
    elif "<@&788840600640290849>" in listamensaje:
            nombre1 = message.author.id

            if nombre1 == 721920162005123142:
                return
            if nombre1 == 757406459167244288:
                return
            elif nombre1 == 758192182389375006:
                return
            elif nombre1 == 734412668789850172:
                return
            elif nombre1 == 656335364256169996:
                return
            else:
                await strikes(message)
                await repormiembros(message)
    elif message.content.startswith('Hola Bien Y Tu? :D'):
        await message.channel.send('Bien, bien :3 Me alegro que estés bien, saluda al Jefe Maestro de mi parte :).')
    elif message.content.startswith('Hola'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Hola, <@' + nombre1 + '>! ¿Cómo estás?')
    elif message.content.startswith('Wenas'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Hola, <@' + nombre1 + '>! ¿Cómo te sientes hoy?')
    elif message.content.startswith('wenas'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Hola, <@' + nombre1 + '>! ¿Todo bien? Me alegro que estés bien :3')
    elif message.content.startswith('Buenas'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Hola, <@' + nombre1 + '>! ¿Cómo te sientes hoy?')
    elif message.content.startswith('buenas'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Hola, <@' + nombre1 + '>! ¿Todo bien? Me alegro que estés bien :3')
    elif message.content.startswith('Buenos dias'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Buenos días, <@' + nombre1 + '>! ¿Todo bien?')
    elif message.content.startswith('Buenos días'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Buenos días, <@' + nombre1 + '>! ¿Cómo va todo?')
    elif message.content.startswith('¡Hola! Soy Cortana.'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Hola, <@' + nombre1 + '>! ¿Cómo va todo?')
    elif message.content.startswith('buenos dias'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Buenos días, <@' + nombre1 + '>! ¿Ya tomaste agüita? :3')
    elif message.content.startswith('buenos días'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Buenos días, <@' + nombre1 + '>!')
    elif message.content.startswith('buen día'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Buen día, <@' + nombre1 + '>! Espero que estés bien ^_^')
    elif message.content.startswith('buen dia'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Buen día, <@' + nombre1 + '>! ¿Ya recargaste tus escudos?')
    elif message.content.startswith('Buen dia'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Buen día, <@' + nombre1 + '>!')
    elif message.content.startswith('Buen día'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Buen día, <@' + nombre1 + '>! No olvides cuidarte de la infección del flood :3')
    if message.content.startswith("no te pregun"):
        await agresivo(message)
    elif message.content.startswith("No te pregun"):
        await agresivo(message)
    elif message.content.startswith("no le pregun"):
        await agresivo(message)
    elif message.content.startswith("No le pregun"):
        await agresivo(message)
    elif message.content.startswith("no me interesa"):
        await agresivo(message)
    elif message.content.startswith("No me interesa"):
        await agresivo(message)
    elif message.content.startswith("chinga tu"):
        await strikes(message)
        await agresivo(message)
    elif message.content.startswith("Chinga tu"):
        await strikes(message)
        await agresivo(message)
    elif message.content.startswith("chingas a tu"):
        await strikes(message)
        await agresivo(message)
    elif message.content.startswith("Chingas a tu"):
        await strikes(message)
        await agresivo(message)
    elif message.content.startswith("chinga a tu"):
        await strikes(message)
        await agresivo(message)
    elif message.content.startswith("Chinga a tu"):
        await strikes(message)
        await agresivo(message)
    elif message.content.startswith("tu put"):
        await strikes(message)
        await agresivo(message)
    elif message.content.startswith("Tu put"):
        await strikes(message)
        await agresivo(message)
    elif message.content.startswith("tu pinc"):
        await strikes(message)
        await agresivo(message)
    elif message.content.startswith("Tu pinc"):
        await strikes(message)
        await agresivo(message)
    elif message.content.startswith("tu col"):
        await strikes(message)
        await agresivo(message)
    elif message.content.startswith("Tu col"):
        await strikes(message)
        await agresivo(message)
    elif message.content.startswith("tu cul"):
        await strikes(message)
        await agresivo(message)
    elif message.content.startswith("Tu cul"):
        await strikes(message)
        await agresivo(message)
    elif message.content.startswith("calle"):
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!721920162005123142>":
            return
        else:
            await agresivo(message)
    elif message.content.startswith("Calle"):
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!721920162005123142>":
            return
        else:
            await agresivo(message)
    elif message.content.startswith("calla"):
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!721920162005123142>":
            return
        else:
            await agresivo(message)
    elif message.content.startswith("Calla"):
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!721920162005123142>":
            return
        else:
            await agresivo(message)
    elif message.content.startswith("se calla"):
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!721920162005123142>":
            return
        else:
            await agresivo(message)
    elif message.content.startswith("Se calla"):
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!721920162005123142>":
            return
        else:
            await agresivo(message)
    elif message.content.startswith("te callas"):
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!721920162005123142>":
            return
        else:
            await agresivo(message)
    elif message.content.startswith("Te callas"):
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!721920162005123142>":
            return
        else:
            await agresivo(message)
    elif message.content.startswith('que hora es'):
        await timehora(message)
    elif message.content.startswith('qué hora es'):
        await timehora(message)
    elif message.content.startswith('que hora son'):
        await timehora(message)
    elif message.content.startswith('qué hora son'):
        await timehora(message)
    elif message.content.startswith('Que hora es'):
        await timehora(message)
    elif message.content.startswith('Qué hora es'):
        await timehora(message)
    elif message.content.startswith('Que hora son'):
        await timehora(message)
    elif message.content.startswith('Qué hora son'):
        await timehora(message)"""
    if message.content.startswith("!ct play"):
        async with message.channel.typing():
          await asyncio.sleep(3)
        await message.reply("Por problemas técnicos se ha deshabilitado temporalmente el comando de música, disculpa :((")
    elif message.content.startswith("!ct loop"):
      if loops == False:
        loops = True
        await message.channel.send("Loop activado")
      else:
        loops = False
        await message.channel.send("Loop desactivado")
    elif message.content.startswith('!ct ayuda'):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await message.reply("El 21 de diciembre de 2021 finalizará el soporte técnico de Citlalmina.")
    elif message.content.startswith('!ct help'):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await message.reply("El 21 de diciembre de 2021 finalizará el soporte técnico de Citlalmina.")
    elif message.content.startswith('!ct palehui'):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await ayuda(message)
    elif message.content.startswith('!ct paleui'):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await ayuda(message)
    elif message.content.startswith('!ct palewi'):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await ayuda(message)
    elif message.content.startswith('!ct palejui'):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await ayuda(message)
    elif message.content.startswith("!ct adhelp"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await adhelp(message)
    elif message.content.startswith("!ct me ama"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await desicionamor(message)
    elif message.content.startswith("!ct abrazo"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await hug(message)
    elif message.content.startswith("!ct abrazar"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await hug(message)
    elif message.content.startswith("!ct hug"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await hug(message)
    elif message.content.startswith("!ct acercade"):
        await message.reply("El 21 de diciembre de 2021 finalizará el soporte técnico de Citlalmina.")
    elif message.content.startswith("!ct acerca de"):
        await message.reply("El 21 de diciembre de 2021 finalizará el soporte técnico de Citlalmina.")
    elif message.content.startswith("!ct kick"):
        await kickear(message)
    elif message.content.startswith("!ct ban"):
        await banear(message)
    elif message.content.startswith("!ct about"):
        await message.reply("El 21 de diciembre de 2021 finalizará el soporte técnico de Citlalmina.")
    elif message.content.startswith('!ct status1'):
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!899835273637167154>":
            await client.change_presence(activity=discord.Game(
                name="!ct ayuda"))
            await message.channel.send('Estado #1 establecido')
        else:
            await message.channel.send(
                'Lo siento, no tienes permiso para ejecutar este comando ^_^')
    elif message.content.startswith('!ct status2'):
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!899835273637167154>":
            await client.change_presence(activity=discord.Activity(
                type=discord.ActivityType.listening, name="ayuda"))
            await message.channel.send('Estado #2 establecido')
        else:
            await message.channel.send(
                'Lo siento, no tienes permiso para ejecutar este comando ^_^')

    elif message.content.startswith('!ct status3'):
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!899835273637167154>":
            await client.change_presence(activity=discord.Activity(
                type=discord.ActivityType.watching, name="a quién ayudar :3"))
            await message.channel.send('Estado #3 establecido')
        else:
            await message.channel.send(
                'Lo siento, no tienes permiso para ejecutar este comando ^_^')
    elif message.content.startswith('!ct status 1'):
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!899835273637167154>":
            await client.change_presence(activity=discord.Game(
                name="!ct ayuda"))
            await message.channel.send('Estado #1 establecido')
        else:
            await message.channel.send(
                'Lo siento, no tienes permiso para ejecutar este comando ^_^')
    elif message.content.startswith('!ct status 2'):
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!899835273637167154>":
            await client.change_presence(activity=discord.Activity(
                type=discord.ActivityType.listening, name="ayuda"))
            await message.channel.send('Estado #2 establecido')
        else:
            await message.channel.send(
                'Lo siento, no tienes permiso para ejecutar este comando ^_^')

    elif message.content.startswith('!ct status 3'):
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!899835273637167154>":
            await client.change_presence(activity=discord.Activity(
                type=discord.ActivityType.watching, name="a quién ayudar :3"))
            await message.channel.send('Estado #3 establecido')
        else:
            await message.channel.send(
                'Lo siento, no tienes permiso para ejecutar este comando ^_^')

    elif message.content.startswith('!ct noticia'):
        # the target we want to open
        url = 'https://www.3djuegos.com/n3/1058/0/halo/'

        #open with GET method
        resp = requests.get(url)

        #http_respone 200 means OK status
        if resp.status_code == 200:
            print("Successfully opened the web page")

            # we need a parser,Python built-in HTML parser is enough .
            soup = BeautifulSoup(resp.text, 'html.parser')

            # l is the list which contains all the text i.e news
            l = soup.find("div", {"class": "s4 c3"})

            #now we want to print only the text part of the anchor.
            #find all the elements of a, i.e anchor
            nott = soup.find_all('article')
            noticion = str(nott[0].text)
            listanot = list(noticion.split("Leer más »"))
            noticiota = str(listanot[0])
            if "Leer más »" in listanot:
                listanot.remove("Leer más »")

            #f = open("noticia.txt","w")
            #f.write(noticiota)
        else:
            print("Error")

        await message.delete()

        embed = discord.Embed(title="Noticia semanal de HALO",
                              description=noticiota,
                              color=discord.Colour.magenta())
        await message.channel.send(embed=embed)


    elif message.content.startswith('!ct beso'):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await besar(message)
    elif message.content.startswith('!ct besar'):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await besar(message)
    elif message.content.startswith('!ct kiss'):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await besar(message)
    #elif message.content.startswith('inquisidor sabe dar masajes en los pies'):
        #await message.channel.send(
            #'Recuerdo cuando mi pelotón me preguntaba eso cuando nuestra misión era cazar al Líder Hereje. Era asqueroso, pero daba sensación de fraternidad.'
        #)
    #elif message.content.startswith('Inquisidor sabe dar masajes en los pies'):
        #await message.channel.send(
            #'Recuerdo cuando mi pelotón me preguntaba eso cuando nuestra misión era cazar al Líder Hereje. Era asqueroso, pero daba sensación de fraternidad.'
        #)
    elif message.content.startswith('!ct meme'):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await desicionmeme(message)
    elif message.content.startswith('!ct ping'):
        await ping(message)
    elif message.content.startswith('takaimayo'):
        await message.channel.send(
            'Watashi wa takaimayo to oniichan aishiteru :3.')
    elif message.content.startswith('Takaimayo'):
        await message.channel.send(
            'Watashi wa takaimayo to oniichan aishiteru :3.')
    elif message.content.startswith("!ct diversity"):
        await message.delete()
        async with message.channel.typing():
          await asyncio.sleep(1)
        await diversity(message)
    elif message.content.startswith("!ct diversidad"):
        await message.delete()
        async with message.channel.typing():
          await asyncio.sleep(1)
        await diversity(message)
    elif message.content.startswith("!ct lgbt"):
        await message.delete()
        async with message.channel.typing():
          await asyncio.sleep(1)
        await diversity(message)
    elif message.content.startswith("!ct lgtb"):
        await message.delete()
        await message.channel.send('La B va antes de la T :3.')
    elif message.content.startswith("!ct LGBT"):
        await message.delete()
        async with message.channel.typing():
          await asyncio.sleep(1)
        await diversity(message)
    elif message.content.startswith("!ct LGTB"):
        await message.delete()
        await message.channel.send('La B va antes de la T :3.')
    elif message.content.startswith("!ct astro"):
        await horoscopo(message)
    elif message.content.startswith("!ct horoscopo"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await horoscope(message)
    elif message.content.startswith("!ct horóscopo"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await horoscope(message)
    elif message.content.startswith("!ct horoscope"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await horoscope(message)
    elif message.content.startswith("!ct invita"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await message.reply("El 21 de diciembre de 2021 finalizará el soporte técnico de Citlalmina.")
      
    elif message.content.startswith("!ct autobiografia"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await auto1(message)
    elif message.content.startswith("!ct autobiografía"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await auto1(message)
    elif message.content.startswith("!ct sobreti"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await sobremi(message)
    elif message.content.startswith("!ct kill"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await matar(message)
    elif message.content.startswith("!ct reboot"):
      nombre1 = str(message.author.id)
      nombre2 = "<@!" + nombre1 + ">"
      if nombre2 == "<@!899835273637167154>":
        mensaje = await message.reply("Reiniciando")
        await asyncio.sleep(1)
        await mensaje.edit(content="Reiniciando.")
        await asyncio.sleep(1)
        await mensaje.edit(content="Reiniciando..")
        await asyncio.sleep(1)
        await mensaje.edit(content="Reiniciando...")
        await asyncio.sleep(1)
        await mensaje.add_reaction("✅")
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
      else:
        async with message.channel.typing():
          await asyncio.sleep(1)
        await message.reply("¡Ese comando sólo es para desarrolladores! >_<")
    elif message.content.startswith("!ct matar"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await matar(message)
    elif message.content.startswith("<@912119451695075338>"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await message.reply("El 21 de diciembre de 2021 finalizará el soporte técnico de Citlalmina.")
    elif message.content.startswith("<@!912119451695075338>"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await message.reply("El 21 de diciembre de 2021 finalizará el soporte técnico de Citlalmina.")
    elif message.content.startswith("!ct 8ball"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await ball(message)
    elif message.content.startswith("!ct bola8"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await ball(message)
    elif message.content.startswith("!ct bolaocho"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await ball(message)
    elif message.content.startswith("!ct bolanegra"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await ball(message)
    elif message.content.startswith("!ct pregúnta"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await ball(message)
    elif message.content.startswith("!ct pregunta"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await ball(message)
    elif message.content.startswith("!ct question"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await ball(message)
    elif message.content.startswith("!ct 8 ball"):
        await message.channel.send(
            "Mira we, si no quieres que explote como lo hizo Chernobyl, pon 8ball, no 8 ball."
        )
    elif message.content.startswith("!ct encuesta"):
        await encuesta(message)
    elif message.content.startswith("!ct poll"):
        await poll(message)
    elif message.content.startswith("!ct vote"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await message.reply("El 21 de diciembre de 2021 finalizará el soporte técnico de Citlalmina.")
    elif message.content.startswith("!ct avatar"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await avatar(message)
    elif message.content.startswith("!ct foto"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await avatar(message)
    elif message.content.startswith("!ct confesion"):
        await confesion(message)
    elif message.content.startswith("!ct confession"):
        await confesion(message)
    elif message.content.startswith("!ct confesión"):
        await confesion(message)
    elif message.content.startswith("!ct yolmelahua"):
        await confesion(message)
    elif message.content.startswith("!ct yolmelaua"):
        await confesion(message)
    elif message.content.startswith("!ct yolmelawa"):
        await confesion(message)
    elif message.content.startswith("!ct compat"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await equipo(message)
    elif message.content.startswith("!ct compat"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await equipo(message)
    elif message.content.startswith("!ct traducir"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await traducir(message)
    elif message.content.startswith("!ct traducción"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await traducir(message)
    elif message.content.startswith("!ct translate"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await translate(message)
    elif message.content.startswith("!ct tradhelp"):
        async with message.channel.typing():
          await asyncio.sleep(1)
        await transhelp(message)
    elif message.content.startswith("!ct del"):
        await eliminar(message)
    elif message.content.startswith("!ct queue"):
        listaqueue = []
        for iterador, cancion in enumerate(playlistdesc, 1):
          listaqueue.append(cancion)
        
        queuefinal = '\n'.join([str(item) for item in listaqueue])

        embed = discord.Embed(title="Cola de reproducción",
                                description=queuefinal,
                                color=discord.Colour.random())
        await message.channel.send(embed=embed)
    #elif message.content.startswith("!ct contar"):
        #await message.channel.send("1")
        #await contar(message)


"""async def timehora(message):

    fmt = '%H:%M:%S %Z'
    d = datetime.datetime.now(pytz.timezone("America/Mexico_City"))
    d_string = d.strftime(fmt)
    d2 = datetime.datetime.strptime(d_string, fmt)
    print (d_string)
    print (d2.strftime(fmt))
    await message.channel.send('Son las ' + d2 + ' en el Valle de México')"""

async def eliminar(message):
  try:
    delt1 = message.content
    if message.author.guild_permissions.manage_messages == True:
      listadel = list(delt1.split(" "))
      n = int(listadel[2])
      await message.delete()
      await message.channel.purge(limit=n)
    else:
      await message.channel.send("Lo siento, no tienes permiso para ejecutar este comando :(( ")
  except:
    await message.channel.send("Escribe el número de mensajes que quieres eliminar :eyes:")

async def desicionamor(message):
    try:
        amor1 = message.content
        listaamor = list(amor1.split(" "))
        desicionlista = [
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"
        ]
        desicion = ""
        desicion = random.choice(desicionlista)
        if desicion == "1":
            await message.channel.send('Sí uwu. ' + listaamor[3] + ' te ama <3')
            desicion = random.choice(desicionlista)
        elif desicion == "2":
            await message.channel.send('No ¬¬. ' + listaamor[3] +
                                       ' no tiene sentimientos >:(')
            desicion = random.choice(desicionlista)
        elif desicion == "3":
            await message.channel.send('Tal vez ' + listaamor[3] +
                                       ' te ama XD.')
            desicion = random.choice(desicionlista)
        elif desicion == "4":
            await message.channel.send('Tal vez ' + listaamor[3] +
                                       ' no te ama ¬¬.')
            desicion = "1"
        elif desicion == "5":
            nombre1 = str(message.author.id)
            await message.channel.send('Puede ser :p. Oye ' + listaamor[3] +
                                       ', ¿amas a <@' + nombre1 + '>? O.O')
            desicion = random.choice(desicionlista)
        elif desicion == "10":
            await message.channel.send('No creo que ' + listaamor[3] +
                                       ' te ame pero ps va XD.')
            desicion = random.choice(desicionlista)
        elif desicion == "7":
            await message.channel.send('Tú y ' + listaamor[3] +
                                       ' son el amor de sus vidas <3.')
            desicion = random.choice(desicionlista)
        elif desicion == "8":
            await message.channel.send('Nah, bien tóxico el ' + listaamor[3] +
                                       ' XD.')
            desicion = random.choice(desicionlista)
        elif desicion == "9":
            nombre1 = str(message.author.id)
            await message.channel.send('Yo les pago la boda pts. <@' +
                                       nombre1 + '>' + ' + ' + listaamor[3])
            desicion = random.choice(desicionlista)
        elif desicion == "10":
            await message.channel.send('Ps... creo que ' + listaamor[3] +
                                       ' sí te ama, pero mejor pregúntale.')
            desicion = random.choice(desicionlista)
        elif desicion == "11":
            await message.channel.send('Tú y ' + listaamor[3] +
                                       ' nacieron para odiarse >:3.')
            desicion = "2"
        elif desicion == "12":
            await message.channel.send('Tú y ' + listaamor[3] +
                                       ' serían una hermosa pareja uwu.')
            desicion = random.choice(desicionlista)
        else:
            await message.channel.send('¿Eh? No entendí. Repite por favor :).')
    except:
        await message.channel.send(
            'Tienes que mencionar a alguien ¬¬.')

async def ayuda(message):
    handler = open('help.txt')
    ayuda1 = handler.read()
    embed = discord.Embed(title="Ayuda de Citlalmina",
                          description=ayuda1,
                          color=discord.Colour.random())
    embed.set_footer(text="v5.8")
    await message.author.send(embed=embed)
    #await message.author.send("𝐈𝐧𝐭𝐥𝐚 𝐭𝐢𝐜𝐧𝐚𝐦𝐢𝐪𝐮𝐢 𝐧𝐨𝐜𝐡𝐢𝐧𝐭𝐢𝐧 𝐢𝐧 𝐢𝐜𝐡𝐭𝐚𝐜𝐚𝐲𝐨𝐦𝐞𝐡, 𝐧𝐢𝐦𝐢𝐭𝐳𝐦𝐚𝐜𝐚𝐳 𝐜𝐞 𝐭𝐞𝐭𝐥𝐚𝐮𝐡𝐭𝐢𝐥𝐥𝐢 :smirk:")
    await message.channel.send("Revisa tu chat privado ^_^")

async def despedida(message):
    handler = open('despedida.txt')
    ayuda1 = handler.read()
    embed = discord.Embed(title="Finalización del soporte técnico de Citlalmina",
                          description=ayuda1,
                          color=discord.Colour.random())
    await message.channel.send(embed=embed)

async def besar(message):
    try:
        besar1 = message.content
        listabesar = list(besar1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        if listabesar[2] == nombre2:
            await message.reply('¿Te besarás a tí mismo? O.o')
        elif listabesar[2] == nombre3:
            await message.reply('¿Te besarás a tí mismo? O.o')
        elif listabesar[2] == "<@!912119451695075338>":
            await message.reply('Ejem... Aquí no, hay niños o///o')
        elif listabesar[2] == "<@912119451695075338>":
            await message.reply('Ejem... Aquí no, hay niños o///o')
        elif listabesar[2] == "<@!906364686428164166>":
            await message.reply('Acércatele y te reviento la cabeza con mi macuahuitl...')
        elif listabesar[2] == "<@906364686428164166>":
            await message.reply('Acércatele y te reviento la cabeza con mi macuahuitl...')
        else:
            await message.channel.send('<@' + nombre1 + '> ha besado a ' +
                                       listabesar[2] + '! :revolving_hearts:')
            await message.delete()
            await gifbeso(message)
    except:
        await message.reply(
            'Tienes que mencionar a alguien ._.')


async def gifbeso(message):
    embed = discord.Embed(title="Citlalmina", color=discord.Colour.magenta())
    linea = ""
    file = copen("besoimagen.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)


async def desicionmeme(message):
        global reddit
        desicionlista = ["MAAU", "memexico", "HaloMemes"]
        desicion = ""
        desicion = random.choice(desicionlista)
        submission = await reddit.subreddit(desicion)
        meme = await submission.random()
        if meme.url.startswith("https://www.reddit.com/"):
          await desicionmeme(message)
        elif meme.url.startswith("https://v.redd.it/"):
          await desicionmeme(message)
        else:
          embed = discord.Embed(title='Meme', color=discord.Colour.random())
          embed.set_image(url=meme.url)
          embed.set_footer(text="Meme de r/" + desicion)
          await message.channel.send(embed=embed)

async def diversity(message):
    nombre1 = str(message.author.id)
    nombre2 = "<@" + nombre1 + ">"
    embed = discord.Embed(
        title="Citlalmina",
        color=discord.Colour.magenta(),
    )
    linea = ""
    file = copen("lgbtqplus.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    embed.set_footer(text="Comando secreto 1/5")
    await message.channel.send(embed=embed)

async def auto1(message):
    handler = open('auto1.txt')
    autobio1 = handler.read()
    embed = discord.Embed(title="Biografía de Citlalmina",
                          description=autobio1,
                          color=discord.Colour.random())
    #message_channel = client.get_channel(803850947734011925)
    await message.channel.send(embed=embed)


async def sobremi(message):

    await message.channel.send(
        "Revisa tu chat privado :3. Comando secreto 4/5.")
    handler = open('auto1.txt')
    sobrethel = handler.read()
    embed = discord.Embed(title="Sobre Citlalmina",
                          description=sobrethel,
                          color=discord.Colour.random())
    #message_channel = client.get_channel(803850947734011925)
    await message.author.send(embed=embed)
    await message.delete()


"""async def espachurrar(message):
    try:
        espa1 = message.content
        listaespa = list(espa1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        if listaespa[2] == nombre2:
            await message.channel.send('¿Te espachurarrás a tí mismo? O.o')
        elif listaespa[2] == nombre3:
            await message.channel.send('¿Te espachurarrás a tí mismo? O.o')
        elif listaespa[2] == "<@!904763964402049074>":
            await message.channel.send(
                'Ejem... Mejor no lo haga compa, si no quiere salir volando hasta Paraguay (que por cierto no existe XD)'
            )
        elif listaespa[2] == "<@904763964402049074>":
            await message.channel.send(
                'Ejem... Mejor no lo haga compa, si no quiere salir volando hasta Paraguay (que por cierto no existe XD)'
            )
        else:
            await message.channel.send('<@' + nombre1 +
                                       '> ha espachurrado a ' + listaespa[2] +
                                       '! O.o')
            await gifespa(message)
    except:
        await message.channel.send(
            'No seas burro. Tienes que mencionar a alguien ._.')


async def gifespa(message):
    embed = discord.Embed(title="Citlalmina", color=discord.Colour.random())
    linea = ""
    file = copen("espachimagen.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)"""


async def matar(message):
    try:
        mat1 = message.content
        listamatar = list(mat1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        if listamatar[2] == nombre2:
            await message.reply(
                'No compa no lo haga, el suic1dio nunca es la opción, tiene muchas razones para vivir :c'
            )
        elif listamatar[2] == nombre3:
            await message.reply(
                'No compa no lo haga, el suic1dio nunca es la opción, tiene muchas razones para vivir :c'
            )
        elif listamatar[2] == "<@!912119451695075338>":
            await message.reply(
                'Acércate pt, vas a ver que te hago caca en 2 segundos con mi macuahuitl...')
        elif listamatar[2] == "<@912119451695075338>":
            await message.reply(
                'Acércate pt, vas a ver que te hago caca en 2 segundos con mi macuahuitl...')
        elif listamatar[2] == "<@!906364686428164166>":
            await message.reply(
                '¡<@906364686428164166> es inmortal! x_x')
        elif listamatar[2] == "<@906364686428164166>":
            await message.reply(
                '¡<@906364686428164166> es inmortal! x_x')
        else:
            await message.channel.send('<@' + nombre1 +
                                       '> le dio en su maiz a ' +
                                       listamatar[2] + '! D:')
            await message.delete()
            await gifmat(message)
    except:
        await message.reply(
            'No seas burro. Si no quieres que te mate yo, tienes que mencionar a alguien ._.'
        )


async def gifmat(message):
    embed = discord.Embed(title="Citlalmina", color=discord.Colour.random())
    linea = ""
    file = copen("mattimagen.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)


"""async def scorpion(message):
    try:
        scor1 = message.content
        listascor = list(scor1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        if listascor[2] == nombre2:
            await message.channel.send('¿Te dispararás a tí mismo? O.o')
        elif listascor[2] == nombre3:
            await message.channel.send('¿Te dispararás a vos mismo? O.o')
        elif listascor[2] == "<@!904763964402049074>":
            await message.channel.send(
                'Ejem... Mejor no lo haga compa, si no quiere explotar ni lo intente...'
            )
        elif listascor[2] == "<@904763964402049074>":
            await message.channel.send(
                'Ejem... Mejor no lo haga compa, intla ahmo timoxittontlanequi ahmo quiyucateyolia...'
            )
        else:
            await message.channel.send('<@' + nombre1 +
                                       '> le ha disparado con un scorpion a ' +
                                       listascor[2] + '! O.o')
            await gifscor(message)
    except:
        await message.channel.send(
            'No seas burro. Tienes que mencionar a alguien ._.')


async def gifscor(message):
    embed = discord.Embed(title="Citlalmina", color=discord.Colour.random())
    linea = ""
    file = copen("scorimagen.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)


async def sniper(message):
    try:
        sniper1 = message.content
        listasniper = list(sniper1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        print(listasniper[2])
        if listasniper[2] == nombre2:
            await message.channel.send('¿Te dispararás a tí mismo? O.o')
        elif listasniper[2] == nombre3:
            await message.channel.send('¿Te dispararás a tí mismo? O.o')
        elif listasniper[2] == "<@!904763964402049074>":
            await message.channel.send(
                'Ejem... Mejor no lo haga compa, si no quiere una bala en su cola ni lo intente...'
            )
        elif listasniper[2] == "<@904763964402049074>":
            await message.channel.send(
                'Ejem... Mejor no lo haga compa, si no quiere una bala en su cola ni lo intente...'
            )
        else:
            await message.channel.send('<@' + nombre1 + '> ha snipeado a ' +
                                       listasniper[2] + '! Bien pro.')
            await gifsniper(message)
    except:
        await message.channel.send(
            'No seas burro. Tienes que mencionar a alguien ._.')


async def gifsniper(message):
    embed = discord.Embed(title="Citlalmina", color=discord.Colour.random())
    linea = ""
    file = copen("sniperimagen.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)


async def teabag(message):
    try:
        tea1 = message.content
        listatea = list(tea1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        if listatea[2] == nombre2:
            await message.channel.send(
                '¿Te vas a chupar los huevos tú mismo? O.o')
        elif listatea[2] == nombre3:
            await message.channel.send(
                '¿Te vas a chupar los huevos vos mismo? O.o')
        elif listatea[2] == "<@!904763964402049074>":
            await message.channel.send('Yo te voy a teabaguear a ti pt.')
        elif listatea[2] == "<@904763964402049074>":
            await message.channel.send('Yo te voy a teabaguear a ti pt.')
        else:
            await message.channel.send('TEABAG FATALITY A ' + listatea[2] +
                                       '!')
            await gifteabag(message)
    except:
        await message.channel.send(
            'No seas burro. Tienes que mencionar a alguien ._.')


async def gifteabag(message):
    embed = discord.Embed(title="Citlalmina", color=discord.Colour.random())
    linea = ""
    file = copen("teaimagen.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)


async def banshee(message):
    try:
        bans1 = message.content
        listabans = list(bans1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        if listabans[2] == nombre2:
            await message.channel.send(
                'A veces eres raro, no entiendo cómo te vas a matar a tí mismo con un banshee xd._.'
            )
        elif listabans[2] == nombre3:
            await message.channel.send(
                'A veces eres raro, ahmo niccaqui kenin timitzmictitiuh in tehuatl niman ica ce banshee xd._.'
            )
        elif listabans[2] == "<@!904763964402049074>":
            await message.channel.send(
                'Vente para acá hijo de tu pm vas a ver quien se muere...')
        elif listabans[2] == "<@904763964402049074>":
            await message.channel.send(
                'Vente para acá hijo de tu pm vas a ver quien se muere...')
        else:
            await message.channel.send('<@' + nombre1 + '> ha matado a ' +
                                       listabans[2] + ' con un Banshee!')
            await gifbans(message)
    except:
        await message.channel.send(
            'No seas burro. Tienes que mencionar a alguien ._.')


async def gifbans(message):
    embed = discord.Embed(title="Citlalmina", color=discord.Colour.random())
    linea = ""
    file = copen("bansimagen.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)


async def granada(message):
    try:
        grans1 = message.content
        listagrans = list(grans1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        await message.delete()
        if listagrans[2] == nombre2:
            await message.channel.send(
                'Yo no lo haría si fuera tú... Comando secreto 5/5')
        elif listagrans[2] == nombre3:
            await message.channel.send(
                'Yo no lo haría si fuera vos... Comando secreto 5/5')
        elif listagrans[2] == "<@!904763964402049074>":
            await message.channel.send(
                'Primero aprende a jugar XD. Comando secreto 5/5')
        elif listagrans[2] == "<@904763964402049074>":
            await message.channel.send(
                'Primero aprende a jugar XD. Comando secreto 5/5')
        else:
            await message.channel.send('<@' + nombre1 + '> ha matado a ' +
                                       listagrans[2] + ' con granadas!')
            await gifgrans(message)
    except:
        await message.channel.send(
            'No seas burro. Tienes que mencionar a alguien ._. Comando secreto 5/5'
        )


async def gifgrans(message):
    embed = discord.Embed(title="Citlalmina", color=discord.Colour.random())
    linea = ""
    file = copen("gransimagen.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    embed.set_footer(text="Comando secreto 5/5")
    await message.channel.send(embed=embed)"""


async def ball(message):
    try:
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        msg = message.content
        mensaje1 = list(msg.split(" "))
        mensaje1.pop(0)
        mensaje1.pop(0)
        mensaje2 = ' '.join([str(item) for item in mensaje1])
        linea = ""
        file = copen("bolaocho.txt")
        lines = file.count('\n')
        random_line = file.getline(randint(1, lines))
        linea = random_line

        embed = discord.Embed(title=":8ball: Citlalmina 8ball",
                              color=discord.Colour.random())
        embed.add_field(name=f":question: {message.author.name} pregunta:",
                        value=mensaje2,
                        inline=False)
        embed.add_field(name=":100: Respuesta de Citlalmina:",
                        value=linea,
                        inline=False)
        await message.channel.send(embed=embed)
        await message.delete()
    except:
        await message.channel.send("We, pero escribe algo._.")


"""async def espada(message):
    try:
        sword1 = message.content
        listasword = list(sword1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        if listasword[2] == nombre2:
            await message.channel.send('¿Te auto espadearás? O.o')
        elif listasword[2] == nombre3:
            await message.channel.send('¿Te auto espadearás? O.o')
        elif listasword[2] == "<@!904763964402049074>":
            await message.channel.send(
                'Ejem... Soy experta con el macuahuitl, si no quieres un madrazo en la cabeza ni te me acerques...'
            )
        elif listasword[2] == "<@904763964402049074>":
            await message.channel.send(
                'Ejem... Soy experta con el macuahuitl, si no quieres un madrazo en la cabeza ni te me acerques...'
            )
        else:
            await message.channel.send('<@' + nombre1 + '> ha espadeado a ' +
                                       listasword[2] + '!')
            await gifsword(message)
    except:
        await message.channel.send(
            'No seas burro. Tienes que mencionar a alguien ._.')


async def gifsword(message):
    embed = discord.Embed(title="Citlalmina", color=discord.Colour.random())
    linea = ""
    file = copen("swordimagen.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)"""


async def encuesta(message):
    try:
        msg = message.content
        mensaje1 = list(msg.split(" "))
        mensaje1.remove("!ct")
        mensaje1.remove("encuesta")
        mensaje2 = ' '.join([str(item) for item in mensaje1])

        embed = discord.Embed(title="Encuesta de Citlalmina",
                              color=discord.Colour.random())
        embed.add_field(name=":question: Encuesta:",
                        value=mensaje2,
                        inline=False)
        embed.add_field(name="Respuesta 1",
                        value=":white_check_mark: Sí",
                        inline=True)
        embed.add_field(name="Respuesta 2", value="⛔ No", inline=True)
        await message.delete()
        message = await message.channel.send(embed=embed)
        await message.add_reaction("✅")
        await message.add_reaction("⛔")
    except:
        await message.channel.send("We, pero escribe algo._.")


async def poll(message):
    try:
        msg = message.content
        mensaje1 = list(msg.split(" "))
        mensaje1.remove("!ct")
        mensaje1.remove("poll")
        mensaje2 = ' '.join([str(item) for item in mensaje1])

        embed = discord.Embed(title="Encuesta de Citlalmina",
                              color=discord.Colour.random())
        embed.add_field(name=":question: Encuesta:",
                        value=mensaje2,
                        inline=False)
        embed.add_field(name="Respuesta 1",
                        value=":white_check_mark: Sí",
                        inline=True)
        embed.add_field(name="Respuesta 2", value="⛔ No", inline=True)
        await message.delete()
        message = await message.channel.send(embed=embed)
        await message.add_reaction("✅")
        await message.add_reaction("⛔")
    except:
        await message.channel.send("We, pero escribe algo._.")

"""async def vote(message):
  global listavote
  global reacciones
  delt1 = message.content
  autor = message.author
  pregunta = list(delt1.split(" "))
  pregunta.pop(0)
  pregunta.pop(0)
  question = ' '.join([str(item) for item in pregunta])
  try:
    await message.channel.send("Escribe un emoji y una frase. Para terminar, escribe 'fin'. Para cancelar, escribe 'cancelar'")
    msg = await client.wait_for('message', timeout=60)
    mensaje = str(msg.content)
    if msg:
      if msg.author == message.author:
        temp = list(mensaje.split(" "))
        if temp[0] == "fin":
          votacion = ' '.join([str(item) for item in listavote])
          embed = discord.Embed(title=question,
                              description=votacion,
                              color=discord.Colour.random())
          message = await message.channel.send(embed=embed)
          i = 0
          while i < len(reacciones):
            await message.add_reaction(reacciones[i])
            i += 1
          listavote=[]
          reacciones=[]
        elif temp[0] == "cancelar":
          await message.channel.send("Cancelado")
          listavote=[]
          reacciones=[]
        elif temp[0] == "Fin":
          votacion = ' '.join([str(item) for item in listavote])
          embed = discord.Embed(title=question,
                              description=votacion,
                              color=discord.Colour.random())
          message = await message.channel.send(embed=embed)
          i = 0
          while i < len(reacciones):
            await message.add_reaction(reacciones[i])
            i += 1
          listavote=[]
          reacciones=[]
        elif temp[0] == "Cancelar":
          await message.channel.send("Cancelado")
          listavote=[]
          reacciones=[]
        else:
          listavote.extend(temp)
          reacciones.append(temp[0])
          await msg.add_reaction("✅")
          await vote(message)
  except asyncio.TimeoutError:
    await message.channel.send("¡Te tardaste mucho! Vuelve a intentarlo")
    listavote = []
    reacciones =[]
  except:
    await message.channel.send("¡Error! Vuelve a intentarlo.")
    listavote = []
    reacciones =[]

async def update(message):
    mensaje = message.content
    embed = discord.Embed(title=":exclamation:Anuncio importante",
                          description=mensaje,
                          color=discord.Colour.random())
    await message.delete()
    await message.channel.send(embed=embed)"""

async def avatar(message):
    try:
        try:
            avatar1 = message.content
            listavatar = list(avatar1.split(" "))
            nombre1 = message.author
            nombre2 = str(listavatar[2])
            nombrelist = list(nombre2.split("<@!"))
            #print(nombrelist)
            nombre4 = str(nombrelist[1])
            nombrelist2 = list(nombre4.split(">"))
            nombre5 = str(nombrelist2[0])
            userid = int(nombre5)
            if userid == 906364686428164166:
              await message.channel.send("Nono, ella no :3")
            else:
              user = await client.fetch_user(userid)
              us = str(user)
              usuario = list(us.split("#"))
              persona = str(usuario[0])
              nombre3 = "Avatar de " + persona
              peticion = f"Pedido por: {message.author.name}"
              pfp = user.avatar_url
              foto = str(pfp)
              embed = discord.Embed(title=nombre3,
                                    url=foto,
                                    color=discord.Colour.random())
              #username = user.name
              embed.set_image(url=pfp)
              embed.set_footer(text=peticion)
              await message.channel.send(embed=embed)
        except:
            nombre4 = str(nombrelist[0])
            nombrelist2 = list(nombre4.split("<@"))
            nombre41 = str(nombrelist2[1])
            nombrelist3 = list(nombre41.split(">"))
            nombre5 = str(nombrelist3[0])
            userid = int(nombre5)
            if userid == 906364686428164166:
              await message.channel.send("Nono, ella no :3")
            else:
              user = await client.fetch_user(userid)
              us = str(user)
              usuario = list(us.split("#"))
              persona = str(usuario[0])
              nombre3 = "Avatar de " + persona
              peticion = f"Pedido por: {message.author.name}"
              pfp = user.avatar_url
              foto = str(pfp)

              embed = discord.Embed(title=nombre3,
                                    url=foto,
                                    color=discord.Colour.random())
              #username = user.name
              embed.set_image(url=pfp)
              embed.set_footer(text=peticion)
              await message.channel.send(embed=embed)
    except:
        nombre3 = f"Avatar de {message.author.name}"
        autor = message.author
        pfp2 = autor.avatar_url
        foto2 = str(pfp2)
        embed = discord.Embed(title=nombre3,
                              url=foto2,
                              color=discord.Colour.random())
        embed.set_image(url=pfp2)
        await message.channel.send(embed=embed)


async def confesion(message):
    try:
        msg = message.content
        mensaje1 = list(msg.split(" "))
        mensaje1.pop(0)
        mensaje1.pop(0)
        mensaje2 = ' '.join([str(item) for item in mensaje1])

        embed = discord.Embed(title="Confesión:",
                              description="_**"+mensaje2+"**_",
                              color=discord.Colour.random())
        await message.channel.send(embed=embed)
        yol = open("yolmelahualiztin.txt", "a")
        yol.write(f"\n{message.author.name}: " + mensaje2)
        yol.close()
        await message.delete()
    except:
        await message.delete()
        await message.channel.send("We, pero escribe algo._.")


async def equipo(message):
    try:
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        msg = message.content
        mensaje1 = list(msg.split(" "))
        usuario = mensaje1[2]
        linea = ""
        file = copen("equipo.txt")
        lines = file.count('\n')
        random_line = file.getline(randint(1, lines))
        linea = random_line
        lin = list(linea.split("\n"))
        if "0" in lin:
            mensaje = "0 % [. . . . . . .] \n**No son compatibles, mejor ni intenten nada..**"
            await message.channel.send(mensaje)
        elif "25" in lin:
            mensaje = "25 % [███ . . . . .]\n**Son muy poco compatibles. Quizás podrían tener algo, pero duraría poco..**"
            await message.channel.send(mensaje)
        elif "50" in lin:
            mensaje = "50 % [████ . . . .]\n**Son compatibles. Tienen 50% de probabilidades de funcionar como pareja.**"
            await message.channel.send(mensaje)
        elif "75" in lin:
            mensaje = "75 % [████████ . . .]\n**Son altamente compatibles. Un pleito por allí y otro por allá, pero todo iría bien..**"
            await message.channel.send(mensaje)
        elif "100" in lin:
            mensaje = "100 % [███████████]\n**Son la media naranja el uno del otro <3.**"
            await message.channel.send(mensaje)


    except:
        await message.channel.send("Pero menciona a alguien mi buen._.")

"""async def espiar(message):
    try:
        espiar1 = message.content
        listaespiar = list(espiar1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        if listaespiar[2] == nombre2:
            await message.channel.send(
                '¿Te apuntarás con un sniper a tí mismo? O.o')
        elif listaespiar[2] == nombre3:
            await message.channel.send(
                '¿Te apuntarás con un sniper a vos mismo? O.o')
        elif listaespiar[2] == "<@!904763964402049074>":
            await message.channel.send('Quita ese sniper de mi cara, xoxotl.')
        elif listaespiar[2] == "<@904763964402049074>":
            await message.channel.send('Quita ese sniper de mi cara, hueyi xoxotl.')
        else:
            await message.channel.send('¡ <@' + nombre1 +
                                       '> tiene en la mira a ' +
                                       listaespiar[2] + ' !')
            await gifespiar(message)
            await asyncio.sleep(30)
            await message.channel.send("¡ " + listaespiar[2] +
                                       ' fue snipeado por <@' + nombre1 +
                                       '> !')
            await gifsniper(message)
    except:
        await message.channel.send(
            'No seas burro. Tienes que mencionar a alguien ._.')


async def gifespiar(message):
    embed = discord.Embed(title="Citlalmina", color=discord.Colour.random())
    linea = ""
    file = copen("sniperimagen.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)


async def wraith(message):
    try:
        scor1 = message.content
        listascor = list(scor1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        if listascor[2] == nombre2:
            await message.channel.send('¿Te dispararás a tí mismo? O.o')
        elif listascor[2] == nombre3:
            await message.channel.send('¿Te dispararás a vos mismo? O.o')
        elif listascor[2] == "<@!904763964402049074>":
            await message.channel.send(
                'Ejem... Mejor no lo haga compa, si no quiere explotar ni lo intente...'
            )
        elif listascor[2] == "<@904763964402049074>":
            await message.channel.send(
                'Ejem... Mejor no lo haga compa, si no quiere explotar ni lo intente...'
            )
        else:
            await message.channel.send(
                '<@' + nombre1 +
                '> le ha disparado una bola enorme de plasma a ' +
                listascor[2] + ' con un wraith! O.o')
            await gifwr(message)
    except:
        await message.channel.send(
            'No seas burro. Tienes que mencionar a alguien ._.')


async def gifwr(message):
    embed = discord.Embed(title="Citlalmina", color=discord.Colour.random())
    linea = ""
    file = copen("wraith.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)


async def rocket(message):
    try:
        rock1 = message.content
        listarock = list(rock1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        if listarock[2] == nombre2:
            await message.channel.send('¿Te dispararás a tí mismo? O.o')
        elif listarock[2] == nombre3:
            await message.channel.send('¿Te dispararás a vos mismo? O.o')
        elif listarock[2] == "<@!904763964402049074>":
            await message.channel.send(
                'Ejem... Mejor no lo haga compa, si no quiere explotar ni lo intente...'
            )
        elif listarock[2] == "<@904763964402049074>":
            await message.channel.send(
                'Ejem... Mejor no lo haga compa, si no quiere explotar ni lo intente...'
            )
        else:
            await message.channel.send('<@' + nombre1 +
                                       '> ha sacado volando a ' +
                                       listarock[2] + ' con un rocket! O.o')
            await gifrock(message)
    except:
        await message.channel.send(
            'No seas burro. Tienes que mencionar a alguien ._.')


async def gifrock(message):
    embed = discord.Embed(title="Citlalmina", color=discord.Colour.random())
    linea = ""
    file = copen("rocket.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)"""


async def about(message):
    handler = open('acercade.txt')
    sobrethel = handler.read()
    embed = discord.Embed(title="Acerca de Citlalmina",
                          description=sobrethel,
                          color=discord.Colour.random())
    #message_channel = client.get_channel(803850947734011925)
    await message.channel.send(embed=embed)

async def hug(message):
    try:
        hug1 = message.content
        listahug = list(hug1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        if listahug[2] == nombre2:
            await message.channel.send('<@' + nombre1 +
                                       '> se ha abrazado a sí mism@! ')
        elif listahug[2] == nombre3:
            await message.channel.send('<@' + nombre1 +
                                       '> se ha abrazado a sí mism@! ')
        elif listahug[2] == "<@!912119451695075338>":
            await message.channel.send(
                'Gracias! :3'
            )
        elif listahug[2] == "<@912119451695075338>":
            await message.channel.send(
                'Tlazohcamati! :3'
            )
        else:
            await message.channel.send('<@' + nombre1 +
                                       '> ha abrazado a ' +
                                       listahug[2] + ' ! :3')
            await message.delete()
            await gifhug(message)
    except:
        await message.channel.send('<@' + nombre1 +
                                       '> se ha abrazado a sí mism@! ')

async def gifhug(message):

    embed = discord.Embed(title="Citlalmina", color=discord.Colour.random())
    linea = ""
    file = copen("abrazo.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)

async def traducir(message):
  try:
    global translator
    msg = message.content
    mensaje1 = list(msg.split(" "))
    mensaje1.pop(0)
    mensaje1.pop(0)
    mensaje2 = ' '.join([str(item) for item in mensaje1])
    translation = translator.translate(mensaje2, dest="es")
    traduccion = f"{translation.text}"
    idioma = f"{translation.src}"
    detector = "Traducido del " + idiomasx[idioma]
    embed = discord.Embed(title="Traducción:",
                          description=traduccion,
                          color=discord.Colour.random()
    )
    embed.set_footer(text=detector)
    await message.reply(embed=embed)
  except:
    await message.reply("Sintaxis: !ct traducir frase")

async def translate(message):
    try: 
        global translator
        msg = message.content
        mensaje1 = list(msg.split(" "))
        ltarget = mensaje1[2]
        if ltarget == "zh":
            ltarget = "zh-cn"
        elif ltarget == "ch":
            ltarget = "zh-tw"
        elif ltarget == "chi":
            ltarget = "zh-cn"
        mensaje1.remove("!ct")
        mensaje1.pop(0)
        mensaje1.pop(0)
        mensaje2 = ' '.join([str(item) for item in mensaje1])
        translation = translator.translate(mensaje2, dest=ltarget)
        traduccion = f"{translation.text}"
        idioma = f"{translation.src}"
        detector = "Translated from " + LANGUAGES[idioma]
        embed = discord.Embed(title="Translation:",
                              description=traduccion,
                              color=discord.Colour.random()
        )
        embed.set_footer(text=detector)
        await message.channel.send(embed=embed)
    except:
        await message.channel.send("Syntax: !ct translate language phrase. Make sure the language is written in ISO format: https://bit.ly/3bNZiBl")

async def transhelp(message):
    handler = open('helplang.txt')
    ayuda1 = handler.read()
    embed = discord.Embed(title="Ayuda de traducción",
                          description=ayuda1,
                          color=discord.Colour.random())
    #message_channel = client.get_channel(803850947734011925)
    await message.author.send(embed=embed)
    await message.channel.send("Revisa tu chat privado.")

async def adhelp(message):
    handler = open('helpad.txt')
    ayuda1 = handler.read()
    embed = discord.Embed(title="Ayuda para administradores",
                          description=ayuda1,
                          color=discord.Colour.random())
    #message_channel = client.get_channel(803850947734011925)
    await message.author.send(embed=embed)
    await message.channel.send("Revisa tu chat privado.")

async def horoscope(message):
      nombre1 = str(message.author.id)
      if nombre1 == "809997899768922142":
        nombre2 = "<@!" + nombre1 + ">"
        amor = str(random.randint(65, 100))
        salud = str(random.randint(65,100))
        suerte = str(random.randint(65,100))
        dinero = str(random.randint(65,100))
        uno = nombre2 + ", estos son los resultados de tu horóscopo:"
        dos = "\n💖 | Amor: " + amor + "%"
        tres = "\n💉 | Salud: " + salud + "%"
        cuatro = "\n🍀 | Suerte: " + suerte + "%"
        cinco = "\n💸 | Dinero: " + dinero + "%"
        await message.reply(uno + dos + tres + cuatro + cinco)
      else:
        nombre2 = "<@!" + nombre1 + ">"
        amor = str(random.randint(0, 100))
        salud = str(random.randint(0,100))
        suerte = str(random.randint(0,100))
        dinero = str(random.randint(0,100))
        uno = nombre2 + ", estos son los resultados de tu horóscopo:"
        dos = "\n💖 | Amor: " + amor + "%"
        tres = "\n💉 | Salud: " + salud + "%"
        cuatro = "\n🍀 | Suerte: " + suerte + "%"
        cinco = "\n💸 | Dinero: " + dinero + "%"
        await message.reply(uno + dos + tres + cuatro + cinco)

async def ping(message):
    antes = time.monotonic()
    mensaje = await message.channel.send(".")
    ping1 = (time.monotonic() - antes)*1000
    ping2 = (str(ping1).split('.'))[0]
    await mensaje.edit(content=ping2 + "ms")
    
async def kickear(message):
  try:
    try:
      delt1 = message.content
      if message.author.guild_permissions.kick_members == True:
        listadel = list(delt1.split(" "))
        usuario = listadel[2]
        listaus1 = list(usuario.split("<@!"))
        usuario2 = listaus1[1]
        listaus2 = list(usuario2.split(">"))
        usuario3 = listaus2[0]
        kickeado = await message.guild.fetch_member(usuario3)
        await message.guild.kick(kickeado, reason=None)
        listo = await message.channel.send("Usuario kickeado.")
        await asyncio.sleep(3)
        await listo.delete()
      else:
        await message.channel.send("Lo siento, no tienes permiso para ejecutar este comando :eyes:. ")
    except:
      delt1 = message.content
      if message.author.guild_permissions.kick_members == True:
        listadel = list(delt1.split(" "))
        usuario = listadel[2]
        listaus1 = list(usuario.split("<@"))
        usuario2 = listaus1[1]
        listaus2 = list(usuario2.split(">"))
        usuario3 = listaus2[0]
        kickeado = await message.guild.fetch_member(usuario3)
        await message.guild.kick(kickeado, reason=None)
        listo = await message.channel.send("Usuario kickeado.")
        await asyncio.sleep(3)
        await listo.delete()
      else:
        await message.channel.send("Lo siento, no tienes permiso para ejecutar este comando :eyes:. ")
  except:
    await message.channel.send("Menciona a quién quieres kickear...")
    
    
async def banear(message):
  try:
    try:
      delt1 = message.content
      if message.author.guild_permissions.ban_members == True:
        listadel = list(delt1.split(" "))
        usuario = listadel[2]
        listaus1 = list(usuario.split("<@!"))
        usuario2 = listaus1[1]
        listaus2 = list(usuario2.split(">"))
        usuario3 = listaus2[0]
        kickeado = await message.guild.fetch_member(usuario3)
        await message.guild.ban(kickeado, reason=None)
        listo = await message.channel.send("Usuario baneado.")
        await asyncio.sleep(3)
        await listo.delete()
      else:
        await message.channel.send("Lo siento, no tienes permiso para ejecutar este comando :eyes:. ")
    except:
      delt1 = message.content
      if message.author.guild_permissions.ban_members == True:
        listadel = list(delt1.split(" "))
        usuario = listadel[2]
        listaus1 = list(usuario.split("<@"))
        usuario2 = listaus1[1]
        listaus2 = list(usuario2.split(">"))
        usuario3 = listaus2[0]
        kickeado = await message.guild.fetch_member(usuario3)
        await message.guild.ban(kickeado, reason=None)
        listo = await message.channel.send("Usuario baneado.")
        await asyncio.sleep(3)
        await listo.delete()
      else:
        await message.channel.send("Lo siento, no tienes permiso para ejecutar este comando :eyes:. ")
  except:
    await message.channel.send("Menciona a quién quieres banear...")

async def horoscopo(message):
    try:
        horosc = message.content
        listahorosc = list(horosc.split(" "))
        horsemanal = ""
        hors = ""
        if "aries" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/aries-hor%C3%B3scopo-diario-gratis/ar-AAyQCeq/'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "Aries" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/aries-hor%C3%B3scopo-diario-gratis/ar-AAyQCeq/'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "tauro" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/tauro-hor%C3%B3scopo-diario-gratis/ar-AAyQHkq'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "Tauro" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/tauro-hor%C3%B3scopo-diario-gratis/ar-AAyQHkq'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "geminis" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/g%C3%A9minis-hor%C3%B3scopo-diario-gratis/ar-AAyQM8E'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "Geminis" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/g%C3%A9minis-hor%C3%B3scopo-diario-gratis/ar-AAyQM8E'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "géminis" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/g%C3%A9minis-hor%C3%B3scopo-diario-gratis/ar-AAyQM8E'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "Géminis" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/g%C3%A9minis-hor%C3%B3scopo-diario-gratis/ar-AAyQM8E'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "cancer" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/c%C3%A1ncer-hor%C3%B3scopo-diario-gratis/ar-AAyQvc6'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "Cancer" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/c%C3%A1ncer-hor%C3%B3scopo-diario-gratis/ar-AAyQvc6'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "cáncer" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/c%C3%A1ncer-hor%C3%B3scopo-diario-gratis/ar-AAyQvc6'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "Cáncer" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/c%C3%A1ncer-hor%C3%B3scopo-diario-gratis/ar-AAyQvc6'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "leo" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/leo-hor%C3%B3scopo-diario-gratis/ar-AAyQEMt'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "Leo" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/leo-hor%C3%B3scopo-diario-gratis/ar-AAyQEMt'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "virgo" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/virgo-hor%C3%B3scopo-diario-gratis/ar-AAyQEMw'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "Virgo" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/virgo-hor%C3%B3scopo-diario-gratis/ar-AAyQEMw'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "libra" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/libra-hor%C3%B3scopo-diario-gratis/ar-AAyQEMC'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "Libra" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/libra-hor%C3%B3scopo-diario-gratis/ar-AAyQEMC'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "escorpio" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/escorpio-hor%C3%B3scopo-diario-gratis/ar-AAyQJBT'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "Escorpio" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/escorpio-hor%C3%B3scopo-diario-gratis/ar-AAyQJBT'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "sagitario" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/sagitario-hor%C3%B3scopo-diario-gratis/ar-AAyQQQv'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "Sagitario" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/sagitario-hor%C3%B3scopo-diario-gratis/ar-AAyQQQv'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "capricornio" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/capricornio-hor%C3%B3scopo-diario-gratis/ar-AAyQHkM'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "Capricornio" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/capricornio-hor%C3%B3scopo-diario-gratis/ar-AAyQHkM'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "acuario" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/acuario-hor%C3%B3scopo-diario-gratis/ar-AAyQwZ9'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "Acuario" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/acuario-hor%C3%B3scopo-diario-gratis/ar-AAyQwZ9'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "piscis" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/piscis-hor%C3%B3scopo-diario-gratis/ar-AAyQvcC'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        elif "Piscis" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open
            url = 'https://www.msn.com/es-mx/estilo-de-vida/horoscopos/piscis-hor%C3%B3scopo-diario-gratis/ar-AAyQvcC'

            #open with GET method
            resp = requests.get(url)

            #http_respone 200 means OK status
            if resp.status_code == 200:
                print("Successfully opened the web page")

                # we need a parser,Python built-in HTML parser is enough .
                soup = BeautifulSoup(resp.text, 'html.parser')

                hor = soup.find_all('p')
                hors = str(hor[0].text)

            else:
                print("Error")

        else:
            await message.delete()
            await message.channel.send(
                "Hmm... Creo que lo escribiste mal, revisa por favor :3.")

        embed = discord.Embed(title=horsemanal,
                              description=hors,
                              color=discord.Colour.magenta())
        piehor = "Más información en: " + url
        embed.set_footer(text="Comando secreto 3/5.")
        await message.author.send(embed=embed)
        await message.author.send(piehor)
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        await message.delete()
        await message.channel.send("Revisa tu chat privado uwu, " + nombre2 +
                                   ". Comando secreto 3/5.")

    except:
        await message.delete()
        await message.channel.send(
            "Escribiste mal el comando, a ver si descubres la forma correcta XD."
        )

client.run('TOKEN')
