import discord
import random
TOKEN = "NzcxNjg2MDYwMjY2NjE4OTAw.X5vupg.uNU1dpbJT-i_MooMpEfhUBmPimw";

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):


    if message.content == '99':
        response = "88"
        await message.channel.send(response)

    if message.content == '88':
        response = "77"
        await message.channel.send(response)

    if message.content == '77':
        response = "66"
        await message.channel.send(response)

    if message.content == '66':
        response = "55"
        await message.channel.send(response)

    if message.content == '55':
        response = "44"
        await message.channel.send(response)

    if message.content == '44':
        response = "33"
        await message.channel.send(response)

    if message.content == '33':
        response = "22"
        await message.channel.send(response)

    if message.content == '22':
        response = "i hope your mikmak acount will get ban:angry: LoL"
        await message.channel.send(response)

    if message.content == "kama ze 1 veod 1":
        lol = ['idk ask ur mom lol', 'haha u stupid', 'you can learn everything in *doofenshmirtz evil incorporated*',
               'to answer that download *simp*ely gitur today', 'check your DM... sike',
               'wait you dont know it,MmM...that means you toxic head poopie xd']


        moivew_item = random.choice(lol)
        await message.channel.send(moivew_item)

    if message.content == 'SteamSales':
        response = "here is today steam sales \n https://store.steampowered.com/search/?specials=1 \n here you go"
        await message.channel.send(response)

    if message.content == 'BeeHelp':
        response = " 1.type *99* for stupid thing \n 2.type *SteamSales* for steam sales today \n 3.type *kama ze 1 veod 1* for more stupid thing \n more commands next if sooshi will not be lazy"
        await message.channel.send(response)

    if message.content == "say a random name":
        lol1 = ['emil', 'mika','tal', 'ariel', 'liroy', 'priel', 'sagie', 'alon', 'elad']


        moivew_item = random.choice(lol1)
        await message.channel.send(moivew_item)

    if message.content == 'Happy birthday':
        response = "88"
        await message.channel.send(response)


client.run(TOKEN)
