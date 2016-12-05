# What's the difference between a List versus a Tuple?

Python carefully distinguishes between several similar concepts:
* set
* list
* tuple
* namedtuple
* iterable, iterator, generator

A `list` is mutable: You can change the elements, add to and remove from the list.  
It's best to use lists for sequences of similar types.  
A `set` efficiently captures similar elements without preserving index position and
repetitions of the same element.

By contrast, a `tuple` is immutable: Fixed elements, fixed size.  
Often, the elements of one tuple have a different type: A different position in 
the tuple expresses a different meaning.  A `namedtuple` expresses this different
meaning by explicit names.  Tuples can be used as keys in a `dict` --- easily and
correctly defining multi-dimensional data structures.

The `iterable` interface expresses just the idea of elements that can be visited
one after another.  It applies to existing data structures --- and also to virtual 
data that is lazily created when needed.  Python works well with infinite iterables.

For any such collection `x  , the function `iter(x)` returns an iterator. 

----

