import pytz
import time
from datetime import datetime, date
import asyncio


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

  await client.change_presence(activity=discord.Game(name="!ct ayuda | " + xihuitl + " " + tonalli))