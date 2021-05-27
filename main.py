import os
import discord
from keep_alive import keep_alive
import requests
import json
#keep_alive Start
keep_alive()

SRC = 'https://github.com/Blazzycrafter/dct/'
PREFIX = '*'



Guild_id = os.environ['Guild_id']

BT = os.environ['UnbelevToken']
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
  elif message.content == f'{PREFIX}work':
#    await message.channel.send('DEACTIVATED')
    headers = {
        'Accept': 'application/json',
        'Authorization': f'{BT}'
    }

    data = '{ "cash": 10}'

    response = requests.patch(f'https://unbelievaboat.com/api/v1/guilds/{Guild_id}/users/{message.author.id}', headers=headers, data=data)
    await message.channel.send(response.text)





client.run(DCToken)