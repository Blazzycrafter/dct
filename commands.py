async def user_commands(message):
    if message.content == f'{PREFIX}src':
        return await message.channel.send(f'SRC: {SRC}')
    