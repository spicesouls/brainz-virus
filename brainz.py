
import discord
from discord.ext import commands
import asyncio
import os
import random
username = os.getlogin()
token = input('Token: ')
prefix = ""
client = discord.Client()
message = discord.Message 
bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.event
async def on_message(message):
    randombrains = random.randint(1,50)
    firstcontent = message.content
    firstcontentlength = len(firstcontent)
    contentbefore = ""
    if firstcontentlength < 3:
        pass
    elif firstcontentlength < 5:
        contentbefore = firstcontent[:2]
    elif firstcontentlength > 5:
        firstcontentnum = random.randint(1, 5)
        contentbefore = firstcontent[:firstcontentnum]
    
    await message.edit(content=contentbefore + "BR" + 'A' * randombrains + "INS")
        

bot.run(token, bot=False)
