# Async functions

Python's `async def` is similar but not identical to JavaScript's `async function`.
Python returns a generator object that can be used only once, not a promise that can 
be used as a meaningful data structure on its own.  You can just `await` the result
of an `async` function.

    import asyncio

    async def slow_operation(n):
        await asyncio.sleep(1)
        print("Slow operation {} complete".format(n))
        return n*2

    async def main():
        print(await slow_operation(1))
        print(await slow_operation(2))
        print(await slow_operation(3))
        
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
