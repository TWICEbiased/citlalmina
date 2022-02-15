from hijri_converter import convert

async def set_date():
  hijri = get_current_hijri()
  await client.change_presence(activity=discord.Game(name=f"!ct ayuda | {hijri}"))

def get_current_hijri():
  hijri = convert.Gregorian.today().to_hijri()
  return f'{hijri.day} {hijri.month_name()} {hijri.year} {hijri.notation(language="en")}'  