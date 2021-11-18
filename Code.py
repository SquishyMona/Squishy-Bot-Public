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
from discord import Member
from discord.ext import commands


os.chdir('[your working directory here]')
logging.basicConfig(level=logging.INFO)

client = discord.Client()
bot = commands.Bot(command_prefix = '$', help_command = None)

bot.Profiles = {}

#Functions that will be used
def saveProfiles():
    with open('Profiles.json', 'w') as file:
        json.dump(bot.Profiles, file)

def createProfile(ctx):
    author = "%s" %ctx.author.id
    bot.Profiles[author] = {}
    bot.Profiles[author]["name"] = ctx.author.display_name
    bot.Profiles[author]["swears"] = 0
    bot.Profiles[author]["level"] = 1
    bot.Profiles[author]["exp"] = 0
    bot.Profiles[author]["sexuality"] = 'Undetermined'
    bot.Profiles[author]["pronouns"] = 'Undetermined'
    saveProfiles()

async def levelingSystem(ctx):
    if ctx.content.startswith('$'):
        return
    exp = bot.Profiles['%s' %ctx.author.id]['exp']
    msgLen = len(ctx.content.split(' '))
    bot.Profiles['%s' %ctx.author.id]['exp'] += msgLen
    
    exp = bot.Profiles['%s' %ctx.author.id]['exp']
    level = bot.Profiles['%s' %ctx.author.id]['level']
    expThreshold = (level * 5) + 5
    if bot.Profiles['%s' %ctx.author.id]['exp'] >= expThreshold:
        bot.Profiles['%s' %ctx.author.id]['level'] += 1
        level = bot.Profiles['%s' %ctx.author.id]['level']
        bot.Profiles['%s' %ctx.author.id]['exp'] = 0
        if level % 5 == 0:
            await ctx.channel.send('Congratulations, %s, you are now level **%d**!' %(ctx.author.display_name, level))

with open("Profiles.json", "r") as file:
    bot.Profiles = json.load(file)

#Console log-in message
@bot.event
async def on_ready():
    print('Session started. User: {0.user}' .format(bot))
    
    game = discord.Game('Squishy Simulator | $help to get started! | ver.0.2b')
    await bot.change_presence(activity = game)
    
    #Lists emoji ID's
    #for emoji in client.emojis:
    #    print("Name: ", emoji.name + ",", "ID: ", emoji.id)
    

@bot.listen('on_message')
async def on_message(message):
    if message.author == bot.user:
        return
    
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
        saveProfiles()
    
    await levelingSystem(message)
    
    saveProfiles()

#Admin Commands
@bot.command(name = 'killbot')
async def killbot(ctx):
    if ctx.author.id == 829418215263436800 or ctx.author.id == 284351113984081922 or ctx.author.id == 335855055095726083:
        await ctx.bot.logout()
    else:
        await ctx.send("Sorry! This is an admin-only command, so peasants like you can't use it! :) 💙 (If you are an admin and would like access to this command, please contact the bot host. Developers: If you'd like access to this command, you can add your User ID to line 136 of the source code.)")

@bot.command(name = 'addprofilefield')
async def addprofilefield(ctx, field, value):
    if ctx.author.id == 284351113984081922:
        await ctx.send('This will add field **%s** with value **%s** to all user profiles. Continue? (y/n) (If any profiles already contain this field, they will be overwritten with value **%s**)' %(field, value, value))
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
                bot.Profiles[items][field] = value  
                
            saveProfiles() 
                
            await ctx.send('Process completed.')
        
    else:
        await ctx.send("Sorry! This is an admin-only command, so peasants like you can't use it! :) 💙 (If you are an admin and would like access to this command, please contact the bot host. Developers: If you'd like access to this command, you can add your User ID to line 136 of the source code.)")
        
@bot.command(name = 'changepresence')
async def changepresence(ctx, *, message):  
    if ctx.author.id == 284351113984081922:
        game = discord.Game(message)
        await bot.change_presence(activity = game)
    else:
        await ctx.send("Sorry! This is an admin-only command, so peasants like you can't use it! :) 💙 (If you are an admin and would like access to this command, please contact the bot host. Developers: If you'd like access to this command, you can add your User ID to line 136 of the source code.)")
    
#Normal Commands
@bot.command(name = 'help')
async def help(ctx):
    await ctx.send('''
Hello, I'm Squishy Bot! I'm currently a work-in-progress, so if you notice any bugs, glitches, or anything else that looks like it probably shouldn't be happening, let me know! Here's a list of commands you can use:

$hit, $pat, and $hug [name]: Does the specified action on another user. [name] can be plain text or an @mention!
$hello: Sends a hello message
$swearcounter: Shows how many times the bot has caught you saying a swear
$profile: Lets you view your profile
$editprofile [field][value]: Lets you edit a section of your profile. Note that some fields cannot be edited, such as your level.
$gaydar: Allows you to use the GayDar
$guessthenumber: A simple number guessing game...or is it?

Looking for admin commands? Try $admin-commands
''')

@bot.command(name = 'hello')
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command(name = 'admin-commands')
async def admincommands(ctx):
    await ctx.send(
        """Here's a list of admin-only commands. (Currently, they're restricted to only be used by Squishy. Role implementation will be added at a later time. Developers: In the mean time, you can add your User ID into the source code at line 136 if you'd like to use these commands)
        
$changepresence [string]: Changes the presence of the bot to whatever you write following the command.
$addprofilefield [field][value]: Adds a new field called [field] to all user profiles with value [value]. **Please note:** Attempting to add an already existing field will **overwrite said field with the specified value on all user profiles.** Please be careful when using this command, as such an action **cannot be undone.**
$killbot: Shuts down the bot.
        """)

@bot.command(name = 'pat')
async def pat(ctx, arg):
    receiver = arg
    print('DEBUG: reciever = %s' %receiver)
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
async def profile(ctx, user: Member = None):
    if user == None:
        author = '%s' %ctx.author.id
        profilePicture = ctx.author.avatar_url
    else:
        profilePicture = user.avatar_url
        author = '%s' %user.id
    
    if author not in bot.Profiles.keys():
        createProfile(ctx)
    
    name = bot.Profiles[author]['name']
    level = bot.Profiles[author]['level']
    exp = bot.Profiles[author]['exp']
    expThreshold = (level * 5) + 5
    swears = bot.Profiles[author]['swears']
    sexuality = bot.Profiles[author]['sexuality']
    pronouns = bot.Profiles[author]['pronouns']
    
    embed = discord.Embed(title = name)
    embed.add_field(name = 'Level', value = level, inline = True)
    embed.add_field(name = 'EXP To Next Level', value = expThreshold - exp, inline = True)
    embed.add_field(name = 'Pronouns', value = pronouns, inline = False)
    embed.add_field(name = 'Sexuality', value = sexuality)
    embed.add_field(name = 'Swears Said', value = swears, inline = False)
    
    embed.set_thumbnail(url=profilePicture)
    embed.set_footer(text = "Command invoked by %s (ID: %s)" %(ctx.author.display_name, ctx.author.id))
    await ctx.send(embed = embed)

@bot.command(name = 'editprofile')
async def editprofile(ctx, field, *, value):
    user = '%s' %ctx.author.id
    if (field == 'level' or field == 'exp' or field == 'swears') or (field not in bot.Profiles[user]):
        await ctx.send("You've entered a field that either does not exist or cannot be edited.")
    elif (field in bot.Profiles[user]) or field == 'Name':
        bot.Profiles[user][field] = value
        saveProfiles()
        await ctx.send('Changes completed! Run "$profile" to double check!')
    

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
        bot.Profiles["%s" %ctx.author.id]['sexuality'] = 'Straight'
    else:
        await ctx.send('You have reached the end. Based on your answers, it has been determined that you are: **GAY.**')
        bot.Profiles["%s" %ctx.author.id]['sexuality'] = 'Gay'
    
    saveProfiles() 
    
    await ctx.send('This quiz determines if you are gay by tallying up **GAY POINTS.** You had **%d** total points.' %gayPoints)

@bot.command(name = 'guessthenumber')
async def guessthenumber(ctx):
    number = ['69', '420']
    answer = random.choice(number)
    print(answer)
    await ctx.send("Welcome to Guess The Number! Seems like a simple and boring game, right? WRONG!!! If you don't guess correctly, **you will be fucking banned from the server.** The stakes are high...are you willing to take the risk? (y/n)")
    def check(response):
        return response.author == ctx.author and response.channel == ctx.channel and (response.content == 'y' or response.content == 'n')
    
    response = await bot.wait_for('message', check=check)
    if response.content == 'n':
        await ctx.send('Understandable.')
        return
    await ctx.send('Then let us continue...you must guess the number I am thinking of. You have two choices: **69** or **420**. Choose wisely...please make your guess.')
    def check(response):
        return response.author == ctx.author and response.channel == ctx.channel and (response.content == '69' or response.content == '420')
    response = await bot.wait_for('message', check=check)
    if response.content == answer:
        await ctx.send('You have answered correctly! Congratulations, you have been spared...for now.')
    else:
        await ctx.send('You have answered...incorrectly...punishment incoming.')
        member = ctx.author
        await member.ban(reason = 'Guessed incorrectly...')

#Sends program information to Discord to be run
bot.run('[your key here]')