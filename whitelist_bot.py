# ota tietyllä text chanelillä käyttäjän teksti ja lisää se toiseen tiedostoon?
# vaihtoehtoisesti lisää toiselle text chanelille?
# googlaa miten botti voi saada napattua käyttäjän viesti ctrl + c tyylisesti

# minechat ja bot keskustelemaan jotta botti voi pelissä kirjottaa pelaajan nimen whitelistiin
# suoraan palvelimelle / miten minechat pääsee palvelimelle kirjoittamaan

import discord
from discord.ext import commands
import time
from discord.ext.commands import Bot
import file_editor
import re

TOKEN = "ODMzNjU4OTU0MTg5NzY2NjY2.YH1jZw.a35L7o2g4c8oorAbb8xSiW6ht1M"

bot = Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=discord.Game('Working hard'))

# search the file if it has the given word in it
@bot.command()
async def search(ctx, *, word: str):
    await ctx.send('Checking File please stand by.')
    with open("demofile.txt", "r") as f:
        searching = re.compile(r'\b({0})\b'.format(word), flags=re.IGNORECASE).search
        line = True
        while line:
            line = f.readline()
            if not line:
                break
            if searching(line):
                await ctx.send("Yes they are in demofile")
                return
    await ctx.send("No they are not in demofile")

# add the given word into the file
@bot.command()
async def add(ctx, *, word: str):
    await ctx.send('Checking File please stand by.')
    with open("demofile.txt", "a") as f:
        f.write(word + '\n')

bot.run(TOKEN)

# for loop käymää rivei läpi ja ettii nickname? jonka perää laittaa teksti
# if tai for loop joka kattoo onko nimi jo siellä
# alla miten whitelist.json tiedost on kirjoitettu

# lisää "name": printtiin ja lainausmerkit tekstin molemmin puolin
"""
[
  {
    "uuid": "f430dbb6-5d9a-444e-b542-e47329b2c5a0",
    "name": "username"
  },
  {
    "uuid": "e5aa0f99-2727-4a11-981f-dded8b1cd032",
    "name": "username"
  }
]
"""