#An example of how to multithread synchronous code (Pillow) in an asynchronous environment (for example discord bots with image generation features) using ThreadPoolExecutor.
import discord
import asyncio
from concurrent.futures import ThreadPoolExecutor
from gen import GenerateImage

POOL = ThreadPoolExecutor()

def ImageFile() -> discord.File:
    return GenerateImage({'OFFER': [[sshf_url, sshf_url, pv_url, skotn_url], robux], 'REQUEST': [[cwhp_url], robux]}) # this URL data should be cached by you or something.
  
async def TradeAdTask(loop):
    result = await loop.run_in_executor(POOL, ImageFile)
    await channel.send(content='Generated Image Test', file=result)
  
async def main():
    loop = asyncio.get_event_loop()
    loop.create_task(TradeAdTask(loop))

                       
asyncio.run(main())
