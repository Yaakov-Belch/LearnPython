# A generator lazily produces a sequence of values:

    def countdown(n):
        while n>0:
           yield n
           n -= 1
    
    for i in countdown(5):
        print(i)
    # 5 4 3 2 1

The result of `g=countdown(3)` is a generator object to be activated 
by `next(g)`:

    g=countdown(3)
    print(g)       # <generator object countdown at 0x7f4cf3cd4410>
    print(next(g)) # 3
    print(next(g)) # 2
    print(next(g)) # 1
    print(next(g)) # StopIteration exception

## Generator pipelines

    def sum(g):
        res=0
        for v in g:
            res += v
        return res;
    
    def squared(g):
        for v in g:
            yield v*v
    
    print(sum(squared(range(10))))  # 285 = 0^2+..+9^2
 
## yield from

Mostly, `yield from g` is a shortcut of `for v in g: yield v`.
However, it opens more channels to pass values through:

* If the generator function returns a value, it can be captured as `v=yield from g`.
* Values sent to a generator will transparently be delegated to the sub-generator.
* Exceptions are passed along transparently.

## Coroutines

Technically, `yield` is a two-way data connection: Any data sent to a generator 
is available as a return value of `yield`.  Coroutines can be used to manage 
asynchronous communication.  However, I find `async` the more appropriate syntax
for this (even though, under the hood, it is implemented with generators).
