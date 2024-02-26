⭐ *I wrote a copy-paste class [`SyncInAsync`](https://github.com/PogoDigitalism/SyncInAsync) for calling non-blocking synchronous functions in asynchronous code!*

## Allows for Pillow image generation in an asynchronous environment without synchronously blocking the event loop.


## how to achieve it:
(check for **async_example.py** in the **examples** folder for a pseudo code showcase of how it works)

- Instance a ThreadPoolExecutor()
- Create an AsyncIO task and assign the image generator function (If you dont want your async function to (asynchronously) yield until the image has been generated. Else just await the run_in_executor coroutine directly)
- Get the current event loop
- await loop.run_in_executor and pass your threadpoolexecutor, (synchronous) image generator function and image configs here
