import discord
import logging
import os
import re
import json
import random
from discord.ext import commands

logging.basicConfig(level=logging.INFO)

client = discord.Client()
bot = commands.Bot(command_prefix = '$')

client.swearCounter = 0
client.gayPoints = 0

#Gets swear counter from txt file
try:
    open("swears.txt", "x").close()
    client.swearCounter = 0
except:
    with open("swears.txt", "r") as file:
        client.swearCounter = int(file.readlines()[0])
       
#Console log-in message
@client.event
async def on_ready():
    print('Session started. User: {0.user}' .format(client))
    
    game = discord.Game('Squishy Simulator | $help to get started!')
    await client.change_presence(activity = game)
    
    #Lists emoji ID's
    #for emoji in client.emojis:
    #    print("Name: ", emoji.name + ",", "ID: ", emoji.id)
    
    
    
#The good shit
@client.event
async def on_message(message):
    
    #Prevents the bot from responding to itself
    if message.author == client.user:
        return
    
    #Help command
    if message.content.startswith('$help'):
        await message.channel.send(
            """Hello! I am Squishy Bot! I'm still a work-in-progress, so if you find any issues, have any feature requests, or have any general feedback, please let Squishy know!\n
(Also Squishy needs more GIFs send some to her fvbjdfjhdthk)
Here's a list of my commands:\n
$hello: Sends a hello message
$pat [name]: Gives anoter user a nice headpat :) 
$attack [name]: Attacks another user
$hug [name]: Gives another user a hug!
$swearcounter: Shows how many times this bot has caught someone saying a swear
            """
        )
    
    #Hello command
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    #Pat command (you'll probably need to change the file paths to match your system)
    if message.content.startswith("$pat"):
        receiver = message.content.split()[1]
        patGIF = [
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/pat/sae_pat.gif', 
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/pat/big-hero6-baymax.gif',
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/pat/bunny.gif',
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/pat/cat.gif',
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/pat/nezuko-yushiro.gif',
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/pat/pat-good-boy.gif',
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/pat/pikachu-pokemon.gif',
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/pat/shark.gif',
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/pat/stitch.gif', 
                 ]
        patGIF = random.choice(patGIF)
        #This part should give you this message if you use the command on yourself but it doesnt work with @mentions
        #for now. Idk how to get that to work so for now you'll have to type your server nickname (case sensitive)
        if(message.author.display_name == receiver):
            await message.channel.send('You patted yourself! You deserve it :)')
        else:
            await message.channel.send('%s patted %s!' %(message.author.display_name, receiver))
        await message.channel.send(file = discord.File(patGIF))
    
    #Attack command    
    if message.content.startswith("$attack"):
        receiver = message.content.split()[1]
        hitGIF = [
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/hit/giorno.gif', 
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/hit/bears.gif',
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/hit/among-us.gif',
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/hit/metatron-god.gif',
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/hit/persona-five.gif',
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/hit/ratio-shin-megami-tensei.gif',
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/hit/runover-kid.gif',
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/hit/stick-figures.gif'
                 ]
        hitGIF = random.choice(hitGIF)
        #This part should give you this message if you use the command on yourself but it doesnt work with @mentions
        #for now. Idk how to get that to work so for now you'll have to type your server nickname (case sensitive)
        if(message.author.display_name == receiver):
            await message.channel.send('You attacked yourself! Not the best life decision...')
        else:
            await message.channel.send('%s fucking attacked the shit out of %s!' %(message.author.display_name, receiver))
        await message.channel.send(file = discord.File(hitGIF))
    
    #Hug command    
    if message.content.startswith("$hug"):
        receiver = message.content.split()[1]
        hugGIF = [
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/hug/ghost.gif', 
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/hug/kh3.gif',
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/hug/marinette.gif',
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/hug/mochi1.gif',
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/hug/mochi2.gif',
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/hug/mona.gif',
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/hug/ralsei-kris.gif',
                    '/Users/squishy/Documents/GitHub/Squishy-Bot/GIFS/hug/cat-hug.gif'
                 ]
        hugGIF = random.choice(hugGIF)
        #This part should give you this message if you use the command on yourself but it doesnt work with @mentions
        #for now. Idk how to get that to work so for now you'll have to type your server nickname (case sensitive)
        if(message.author.display_name == receiver):
            await message.channel.send('You hugged yourself! Self care is important :)')
        else:
            await message.channel.send('%s hugged %s!' %(message.author.display_name, receiver))
        await message.channel.send(file = discord.File(hugGIF))
     
    #Swear counter command. Right now this isn't server or user specific. Idk how to keep track of certain users
    #data yet   
    if message.content.startswith('$swearcounter'):
        await message.channel.send('We have said %d swears.' %(client.swearCounter))   
                        
                                   
        
    #Admin commands. Change the author id to your own to get it to work for you.
    if message.content.startswith('$changepresence'):    
        if message.author.id == 284351113984081922:
            game = discord.Game(message.content[15:])
            await client.change_presence(activity = game)
        else:
            await message.channel.send("Sorry! This is an dev-only command, so peasants like you can't use it! :) 💙")
              
    #Defining commands/trigger messages. Any message that contains these trigger words(or part of them)
    #will trigger its subsequent bot message 
    pattern_re = re.compile(r'pog', re.IGNORECASE)
    pattern_re2 = re.compile(r'meme', re.IGNORECASE)
    pattern_re3 = re.compile(r'troll', re.IGNORECASE)
    pattern_re4 = re.compile(r'pepper pig', re.IGNORECASE)
    #pattern_re5 = re.compile(r"im", re.IGNORECASE) #(This command is broken, so it's commented until I fix it)
    pattern_re6 = re.compile(r"fuck", re.IGNORECASE)
    pattern_re7 = re.compile(r"shit", re.IGNORECASE)
    pattern_re8 = re.compile(r"bitch", re.IGNORECASE)
    pattern_re9 = re.compile(r"crap", re.IGNORECASE)
    pattern_re10 = re.compile(r"hell", re.IGNORECASE)
    pattern_re11 = re.compile(r"damn", re.IGNORECASE)
    
    #Triggers for bot messages
    if re.search(pattern_re, message.content):
        await message.channel.send("did someone say....POG???")
    if re.search(pattern_re2, message.content):
        await message.channel.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    if re.search(pattern_re3, message.content):
         await message.channel.send(file=discord.File('/Users/squishy/Documents/GitHub/Squishy-Bot/Trollface.png'))
    if re.search(pattern_re4, message.content):
        await message.channel.send('https://youtu.be/M3t6kXOcxRc')
    #'response' only displays the next word after 'I'm', not the entire message after.         
    #if re.search(pattern_re5, message.content):
    #    response = message.content.split()[1]
    #    await message.channel.send("Hi " + response + ", I'm Dad!")
    if(
        re.search(pattern_re6, message.content) or 
        re.search(pattern_re7, message.content) or 
        re.search(pattern_re8, message.content) or 
        re.search(pattern_re9, message.content) or 
        re.search(pattern_re10, message.content) or 
        re.search(pattern_re11, message.content)
        ):
        client.swearCounter = client.swearCounter + 1
    
    #Writes to the swearcounter file so it doesn't reset after the bot shuts down
    file = open("swears.txt", "w")
    file.write(str(client.swearCounter))
    file.close()

#Sends program information to Discord to be run
client.run(key)