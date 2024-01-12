#An example of how to handle synchronous code (Pillow) in an asynchronous environment using ThreadPoolExecutor.

import asyncio
from concurrent.futures import ThreadPoolExecutor
from assets.gen import GenerateImage
from assets.config import IMAGE_PARAMS

POOL = ThreadPoolExecutor()
  
async def task_ImageGeneration(loop):
    result = await loop.run_in_executor(executor=POOL, func=GenerateImage, IMAGE_PARAMS) # Replace GenerateImage and ImageConfigs with your own synchronous Pillow image generator function and configuration
    # do whatever with 'result' here

async def main():
    loop = asyncio.get_event_loop()

    loop.create_task(task_ImageGeneration(loop)) # create a task if you dont want the execution of main() to be yielded (asynchronously), else just call loop.run_in_executor here directly.


asyncio.run(main())
