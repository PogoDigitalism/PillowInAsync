import discord
import asyncio
from concurrent.futures import ThreadPoolExecutor
from gen import GenerateImage

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
POOL = ThreadPoolExecutor()

async def TradeAdTask(loop: asyncio.AbstractEventLoop, message: discord.Message):
    result = await loop.run_in_executor(POOL, GenerateImage, {'OFFER': [['https://tr.rbxcdn.com/358b33371dada05e1cd5b14a654aa59a/420/420/Hat/Png', 'https://tr.rbxcdn.com/6a5c38ecedfcefc5e79f292080797596/420/420/Hat/Png'], 10, 35009], 'REQUEST': [['https://tr.rbxcdn.com/8f62abaf50334be5ea1d08040ba35152/420/420/Hat/Png'], 12, 50000]})
    await message.channel.send(content='Generated Image Test', file=result)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        loop = asyncio.get_event_loop()
        loop.create_task(TradeAdTask(loop, message))

        await message.channel.send('Generating image for you..')

client.run('token_here')
