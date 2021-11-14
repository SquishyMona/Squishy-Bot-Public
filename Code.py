# Squishy Bot (Beta)
# Version 0.1b
# Built using discord.py (Learn more at https://discordpy.readthedocs.io/en/stable/)
# 
# This is a fairly simple Discord bot that I'm working on as a side-project during my time in college. I'm gradually
# adding new features as my knowledge of Python and programming as a whole grows, and I've been having a ton of fun
# with it :)

import discord
import logging
import os
import re
import json
import random
from random import randint
from discord.ext import commands


os.chdir('[your working directory here]')
logging.basicConfig(level=logging.INFO)

client = discord.Client()
bot = commands.Bot(command_prefix = '$')

bot.Profiles = {}
def createProfile(ctx):
    author = "%s" %ctx.author.id
    bot.Profiles[author] = {}
    bot.Profiles[author]["name"] = ctx.author.display_name
    bot.Profiles[author]["swears"] = 0
    bot.Profiles[author]["level"] = 1
    bot.Profiles[author]["exp"] = 0
    bot.Profiles[author]["isGay"] = 'Undetermined'
    with open('Profiles.json', 'w') as file:
        json.dump(bot.Profiles, file)

with open("Profiles.json", "r") as file:
    bot.Profiles = json.load(file)

#Console log-in message
@bot.event
async def on_ready():
    print('Session started. User: {0.user}' .format(bot))
    
    game = discord.Game('Squishy Simulator | $help to get started! | ver.0.1b')
    await bot.change_presence(activity = game)
    
    #Lists emoji ID's
    #for emoji in client.emojis:
    #    print("Name: ", emoji.name + ",", "ID: ", emoji.id)
    
#Listener for various messages that aren't commands.
@bot.listen('on_message')
async def on_message(message):
    #Defining trigger messages. Any message that contains these trigger words (or part of them)
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
         await message.channel.send(file=discord.File('Trollface.png'))
    if re.search(pattern_re4, message.content):
        await message.channel.send('https://youtu.be/M3t6kXOcxRc')
    #if re.search(pattern_re5, message.content):
    #    response = message.content[2:]
    #    await message.channel.send("Hi " + response + ", I'm Dad!")
    if(re.search(pattern_re6, message.content) or re.search(pattern_re7, message.content) or re.search(pattern_re8, message.content) or re.search(pattern_re9, message.content) or re.search(pattern_re10, message.content) or re.search(pattern_re11, message.content)):
        bot.Profiles["%s" %message.author.id]['swears'] += 1
        with open('Profiles.json', 'w') as file:
            json.dump(bot.Profiles, file)

#Admin Commands
@bot.command(name = 'addprofilefield')
async def addprofilefield(ctx, arg, arg2):
    if ctx.author.id == 284351113984081922:
        await ctx.send('This will add field **%s** with value **%s** to all user profiles. Continue? (y/n) (If any profiles already contain this field, they will be overwritten with value **%s**' %(arg, arg2, arg2))
        def check(response):
            return (
                response.channel == ctx.channel and 
                response.author == ctx.author and
                (
                    response.content == 'y' or
                    response.content == 'n'
                )
            )
        response = await bot.wait_for('message', check=check)
        if response.content == 'n':
            await ctx.send('Process aborted.')
        else:
            for items in bot.Profiles:
                bot.Profiles[items][arg] = arg2  
                
            with open('Profiles.json', 'w') as file:
                json.dump(bot.Profiles, file)  
                
            await ctx.send('Process completed.')
        
    else:
        await ctx.send("Sorry! This is an admin-only command, so peasants like you can't use it! :) 💙 (If you are an admin and would like access to this command, please contact the bot host. Developers: If you'd like to use this command, you can add your User ID to the 'if' statement directly following the async definition.)")
        
@bot.command(name = 'changepresence')
async def changepresence(ctx, *, message):  
    if ctx.author.id == 284351113984081922:
        game = discord.Game(message)
        await bot.change_presence(activity = game)
    else:
        await ctx.send("Sorry! This is an admin-only command, so peasants like you can't use it! :) 💙 (If you are an admin and would like access to this command, please contact the bot host. Developers: If you'd like to use this command, you can add your User ID to the 'if' statement directly following the async definition.)")
             
    
#Normal Commands
@bot.command(name = 'hello')
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command(name = 'admin-commands')
async def admincommands(ctx):
    await ctx.send(
        """Here's a list of admin-only commands. (Currently, they're restricted to only be used by Squishy. Role implementation will be added at a later time. Developers: If you'd like to use these commands, you can add your User ID to the 'if' statement directly following the async definitions of the various commands.)
        
$changepresence [string]: Changes the presence of the bot to whatever you write following the command.
$addprofilefield [name]: Adds a new field called [name] to all user profiles
        """)

@bot.command(name = 'pat')
async def pat(ctx, arg):
    receiver = arg
    patGIF = [
                'GIFS/pat/sae_pat.gif', 
                'GIFS/pat/big-hero6-baymax.gif',
                'GIFS/pat/bunny.gif',
                'GIFS/pat/cat.gif',
                'GIFS/pat/nezuko-yushiro.gif',
                'GIFS/pat/pat-good-boy.gif',
                'GIFS/pat/pikachu-pokemon.gif',
                'GIFS/pat/shark.gif',
                'GIFS/pat/stitch.gif', 
             ]
    patGIF = random.choice(patGIF)
    await ctx.send('%s patted %s!' %(ctx.author.display_name, receiver))
    await ctx.send(file = discord.File(patGIF))

@bot.command(name = 'hit')
async def hit(ctx, arg):
    receiver = arg
    hitGIF = [
                'GIFS/hit/giorno.gif', 
                'GIFS/hit/bears.gif',
                'GIFS/hit/among-us.gif',
                'GIFS/hit/metatron-god.gif',
                'GIFS/hit/persona-five.gif',
                'GIFS/hit/ratio-shin-megami-tensei.gif',
                'GIFS/hit/runover-kid.gif',
                'GIFS/hit/stick-figures.gif'
             ]
    hitGIF = random.choice(hitGIF)
    await ctx.send('%s fucking attacked the shit out of %s!' %(ctx.author.display_name, receiver))
    await ctx.send(file = discord.File(hitGIF))

@bot.command(name = 'hug')
async def hug(ctx, arg):
    receiver = arg
    hugGIF = [
                'GIFS/hug/ghost.gif', 
                'GIFS/hug/kh3.gif',
                'GIFS/hug/marinette.gif',
                'GIFS/hug/mochi1.gif',
                'GIFS/hug/mochi2.gif',
                'GIFS/hug/mona.gif',
                'GIFS/hug/ralsei-kris.gif',
                'GIFS/hug/cat-hug.gif'
             ]
    hugGIF = random.choice(hugGIF)
    await ctx.send('%s hugged %s!' %(ctx.author.display_name, receiver))
    await ctx.send(file = discord.File(hugGIF))
    
@bot.command(name = 'swearcounter')
async def swearcounter(ctx):
    bot.author_swears = bot.Profiles['%s' %ctx.author.id]['swears']
    if  bot.author_swears != 0:
        await ctx.send('You have said %d swears.' %(bot.author_swears))
    else:
        await ctx.send("You have never said a swear! Wack...")  

@bot.command(name = 'profile')
async def profile(ctx):
    author = '%s' %ctx.author.id
    
    if author not in bot.Profiles.keys():
        createProfile(ctx)
    
    name = bot.Profiles[author]['name']
    level = bot.Profiles[author]['level']
    exp = bot.Profiles[author]['exp']
    swears = bot.Profiles[author]['swears']
    isGay = bot.Profiles[author]['isGay']
    profilePicture = ctx.author.avatar_url
    embed = discord.Embed(title = name)
    embed.add_field(name = 'Level', value = level, inline = True)
    embed.add_field(name = 'Experience', value = exp, inline = True)
    embed.add_field(name = 'Swears Said', value = swears, inline = False)
    embed.add_field(name = 'Is Gay', value = isGay)
    embed.set_thumbnail(url=profilePicture)
    embed.set_footer(text = "Command invoked by %s (ID: %s)" %(ctx.author.display_name, ctx.author.id))
    await ctx.send(embed = embed)

@bot.command(name = 'editprofile')
async def editprofile(ctx, field, value):
    user = '%s' %ctx.author.id
    if (field == 'level' or field == 'exp' or field == 'isGay' or field == 'swears') or (field not in bot.Profiles[user]):
        await ctx.send("You've entered a field that either does not exist or cannot be edited.")
    elif (field in bot.Profiles[user]) or field == 'Name':
        bot.Profiles[user][field] = value
        with open('Profiles.json', 'w') as file:
            json.dump(bot.Profiles, file)
        await ctx.send('Changes completed! Run "$profile" to double check!')
    
#The Gay Detector, aka the GayDar.
@bot.command(name = 'gaydar')
async def gaydar(ctx):
    gayPoints = 0
    scoreFucker = randint(1, 5)
    gayPoints += scoreFucker
    await ctx.send(
'''
Welcome to The Gay Detector, aka the GayDar!
----------------------------------------------------------
This command was developed by Squishy Software Enterprises. 
This implementation is based off of the original "The Gay Detetctor" written in C++.
----------------------------------------------------------
**!!!WARNING!!!**
Before continuing, please note that this program will detect whether you are gay or not **with 100 percent accuracy.** If you are not prepared for the results, please do not continue.
----------------------------------------------------------
Would you like to continue? (y/n)
'''
    )
    def check(response):
        return response.channel == ctx.channel and response.author == ctx.author and (response.content == 'y' or response.content == 'n')
    
    response = await bot.wait_for('message', check=check)
    if response.content == 'n':
        await ctx.send('Weakling.')
        return
    await ctx.send('''You will be asked a series of 10 questions. Please answer "y" for yes or "n" for no for each question. After you have answered all questions, the program will determine whether or not you are gay.
-----------------------------------------------------------
Question 1: Are you attracted to people of the same gender?''')
    
    response = await bot.wait_for('message', check=check)
    if response.content == 'y':
        gayPoints += 5
    
    await ctx.send('Question 2: Did you hesitate answering the previous question?')
    response = await bot.wait_for('message', check=check)
    if response.content == 'y':
        gayPoints += 1
    
    await ctx.send('Question 3: Do you think it is gay to kiss the homies?')
    response = await bot.wait_for('message', check=check)
    if response.content == 'y':
        gayPoints += 2
        
    await ctx.send('Question 4: Do you play Super Smash Bros. Ultimate on the Nintendo Switch??')
    response = await bot.wait_for('message', check=check)
    if response.content == 'y':
        gayPoints += 2
        
    await ctx.send('Question 5: Do your friends often tell you that you look "submissive and breedable"?')
    response = await bot.wait_for('message', check=check)
    if response.content == 'y':
        gayPoints += 3
        
    await ctx.send('Question 6: Are you afraid that this program will expose your homosexuality?')
    response = await bot.wait_for('message', check=check)
    if response.content == 'y':
        gayPoints += 2
        
    await ctx.send('Question 7: Would you engage in sexual activity with the opposite gender?')
    response = await bot.wait_for('message', check=check)
    if response.content == 'n':
        gayPoints += 5
        
    await ctx.send('Question 8: Are you attracted to Dwayne "The Rock" Johnson?')
    response = await bot.wait_for('message', check=check)
    if response.content == 'y':
        gayPoints += 4
        
    await ctx.send('Question 9: Do you like Oreos?')
    response = await bot.wait_for('message', check=check)
    if response.content == 'y':
        gayPoints -= 3
        
    await ctx.send('Question 10: Are you ready to find out if you are gay?')
    response = await bot.wait_for('message', check=check)
    if response.content == 'n':
        gayPoints += 3
        
    if (gayPoints < 15):    
        await ctx.send('You have reached the end. Based on your answers, it has been determined that you are: **NOT GAY.**')
        bot.Profiles["%s" %ctx.author.id]['isGay'] = 'No'
    else:
        await ctx.send('You have reached the end. Based on your answers, it has been determined that you are: **GAY.**')
        bot.Profiles["%s" %ctx.author.id]['isGay'] = 'Yes'
    
    with open('Profiles.json', 'w') as file:
                json.dump(bot.Profiles, file)  
    
    await ctx.send('This quiz determines if you are gay by tallying up **GAY POINTS.** You had **%d** total points.' %gayPoints)


    
#Unimplimented commands from old system (these don't run right now.)
@client.event
async def on_message(message):

    if message.content.startswith('$view-profile'):
        profile = message.content[9:]
        for keys in client.Profiles.keys():
            print('DEBUG: Key = %s' %keys)
            if client.Profiles[keys]["name"] == profile:
                profile = keys
                print('DEBUG: "profile" = %s' %profile)
            else:
                await message.channel.send("User not found. Make sure you typed their user name **exactly as it appears on their profile.**")
                break
            
        name = client.Profiles[profile]['name']
        level = client.Profiles[profile]['level']
        exp = client.Profiles[profile]['exp']
        swears = client.Profiles[profile]['swears']
        profilePicture = profile.avatar_url
        embed = discord.Embed(title = name)
        embed.add_field(name = 'Level', value = level, inline = True)
        embed.add_field(name = 'Experience', value = exp, inline = True)
        embed.add_field(name = 'Swears Said', value = swears, inline = False)
        embed.set_thumbnail(url=profilePicture)
        embed.set_footer(text = "Command invoked by %s (ID: %s)" %(message.author.display_name, message.author.id))
        await message.channel.send(embed = embed)
            

#Sends program information to Discord to be run
bot.run('[your key here]')