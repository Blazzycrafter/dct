import os
import discord
from keep_alive import keep_alive
from replit import db

#keep_alive Start
keep_alive()

SRC = 'https://github.com/Blazzycrafter/dct/'
try:
    PREFIX = db["PREFIX"]
except:
    db["PREFIX"] = "*"
    PREFIX = db["prefix"]

DCToken = os.environ['TOKEN']
client = discord.Client()



@client.event
async def on_ready():
  print('We have logged in as User: {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    print('ME: '+ message.content)
    return
  else:
    print(str(message.author) +': '+ message.content)
  
  if message.content == f'{PREFIX}src':
    await message.channel.send(f'SRC: {SRC}')
  if message.content == f'{PREFIX}setprefix':
    await message.channel.send('WIP')




client.run(DCToken)