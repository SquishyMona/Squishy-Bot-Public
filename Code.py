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

client.swearCounter = {}
client.gayPoints = 0

with open("swears-users.json", "r") as file:
    client.swearCounter = json.load(file)
       
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
    
    #Sample commands w/ prefix
    if message.content.startswith('$help'):
        await message.channel.send(
            """Hello! I am Squishy Bot! I'm still a work-in-progress, so if you find any issues, have any feature requests, or have any general feedback, please let Squishy know!\n
Here's a list of my commands:\n
$hello: Sends a hello message
$pat [name]: Gives anoter user a nice headpat :) (Squishy needs more GIFs send some to her fvbjdfjhdthk)
$hit [name]: Attacks another user (Squishy needs more GIFs send some to her fvbjdfjhdthk)
$swearcounter: Shows how many times this bot has caught someone saying a swear
            """
        )
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
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
        await message.channel.send('%s patted %s!' %(message.author.display_name, receiver))
        await message.channel.send(file = discord.File(patGIF))
        
    if message.content.startswith("$hit"):
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
        await message.channel.send('%s fucking attacked the shit out of %s!' %(message.author.display_name, receiver))
        await message.channel.send(file = discord.File(hitGIF))
        
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
        await message.channel.send('%s hugged %s!' %(message.author.display_name, receiver))
        await message.channel.send(file = discord.File(hugGIF))
        
    if message.content.startswith('$swearcounter'):
        if message.author.id in client.swearCounter:
            await message.channel.send('You have said %d swears.' %(client.swearCounter["%d" %message.author.id]))   
        else:
            await message.channel.send("You have never said a swear! Wack...")            
                                   
        
    #Admin commands
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
    #pattern_re5 = re.compile(r"i'm", re.IGNORECASE)
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
    #if re.search(pattern_re5, message.content):
    #    response = message.content[2:]
    #    await message.channel.send("Hi " + response + ", I'm Dad!")
    if(re.search(pattern_re6, message.content) or re.search(pattern_re7, message.content) or re.search(pattern_re8, message.content) or re.search(pattern_re9, message.content) or re.search(pattern_re10, message.content) or re.search(pattern_re11, message.content)):
        swearer = "%d" %message.author.id
        if swearer in client.swearCounter.keys():
            client.swearCounter[swearer] += 1
        else:
            client.swearCounter[swearer] = 1
    
   
    
    with open('swears-users.json', 'w') as file:
        json.dump(client.swearCounter, file)
    
    
    

#Sends program information to Discord to be run
client.run(key)