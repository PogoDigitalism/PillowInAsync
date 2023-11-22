#An example of how to handle synchronous code (Pillow) in an asynchronous environment using ThreadPoolExecutor.

# !! This example is *PSEUDO-ish CODE*

import discord
import asyncio
from concurrent.futures import ThreadPoolExecutor
from gen import GenerateImage

POOL = ThreadPoolExecutor()
  
async def task_ImageGeneration(loop):
    result = await loop.run_in_executor(POOL, GenerateImage, ImageConfigs) # Replace GenerateImage and ImageConfigs with your own synchronous Pillow image generator function and configuration
  
async def main():
    loop = asyncio.get_event_loop()
    loop.create_task(task_ImageGeneration(loop)) # create a task if you dont want the execution of main() to be yielded , else just call loop.run_in_executor here directly.


asyncio.run(main())
