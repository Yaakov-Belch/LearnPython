# A generator lazily produces a sequence of numbers:

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
 
