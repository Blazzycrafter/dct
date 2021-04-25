import os
import discord
from keep_alive import keep_alive
from commands import user_commands

#keep_alive Start
keep_alive()

SRC = 'https://github.com/Blazzycrafter/dct/'
PREFIX = '*'


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
  
  if message.content.startswith == f'{PREFIX}':
    await user_commands(message)





client.run(DCToken)