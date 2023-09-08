from ayarlar import ayarlar
import discord
from bot_mantik import *

ayricaliklar = discord.Intents.default()
ayricaliklar.message_content = True
istemci = discord.Client(intents=ayricaliklar)


@istemci.event
async def on_ready():
    print(f'{istemci.user} olarak giriş yaptık')


@istemci.event
async def on_message(message):
    if message.author == istemci.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Selam! Ben bir botum!')
    elif message.content.startswith('$smile'):
        await message.channel.send(emoji_olusturucu())
    elif message.content.startswith('$coin'):
        await message.channel.send(yazi_tura())
    elif message.content.startswith('$pass'):
        await message.channel.send(sifre_olusturucu(10))
    elif message.content.staetswith('Zar At'):
        await message.content.send(zar_at)
    else:
        await message.channel.send("Bu komutu anlayamadım :(")

istemci.run(ayarlar["TOKEN"])
