import discord, random
from bot_logic import gen_pass

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

def mesajger():
    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')
    
    @client.event
    async def on_message(message):
        if message.content.startswith('hello'):
            await message.channel.send("Hi!")
        elif message.content.startswith('$bye'):
            await message.channel.send("\\U0001f642")
        elif message.content.startswith('$yazıturaat'):
            problem = random.choice(('yazı', 'tura'))
            await message.channel.send(problem)
        elif message.content.startswith('Yapay Zeka Arkadaşım'):
            await message.channel.send('Şu an yetkim yok :)')
    
    client.run("MTE0NDY1ODg2MTI0MDg4OTQwNQ.G0xiCL.S6xDVXYN-T0Q0eFzSLQvCfUovfleSxa1YLe05E")


mesajger()
