# Async functions

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

In Python, `async` functions return generators. They can be `await`ed only once.

In JavaScript, `async` functions return promises. To me, this seems more generally
usable: Promises can be shared consistently, there are many promise-based algorithms and 
abstractions.
