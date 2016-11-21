# Questions

## How do I convert a string to a number?
Python does not automatically convert strings to numbers.  
This is less convenient than perl on receiving data input.
But it is more correct and precise in many cases:

* Detect input format errors early.
* Correctly sort, add, multiply numbers vs. strings

Verify that mixed number/string operations (compare, sort, 
add) raise errors.

### How do I convert a number to a string?

## How should I represent data in python programs?

**Baby python:** You can express almost all algorithms
with the basic JSON structures: numbers, strings, lists,
and dicts (dictionaries).

**Python types:** Python provides more explicit types
that make your programs clearer --- and make it easier
to do the right thing right: `None`, `True`, `False`, 
sets, tuples, objects.

**Lazy sequences (iterables and iterators):** Python 
extensively supports iterables.  You can loop over 
sequences without allocating memory for them.  Express 
algorithms with infinite sequences and use only as much 
of them as needed.

**NumPy arrays:** Large, multi-dimensional arrays of 
numbers can be stored efficiently and compactly as numpy
arrays.

## How do I use regular expressions?

* check match
* extract matching groups
* replace matches by strings or function results
* extended regexp features

# Topics

* regular expressions
* flow control: break continue
* OOP, class definitions
* functions of the standard library
* list and dict comprehensions
* ecpeption handling: try raise
* numpy
* tensorflow
* None
* unpacking assignment, multiple return values

Data libraries
* [NumPy](http://www.numpy.org/)
* [Pandas](http://pandas.pydata.org/)
* [StatsModels](http://statsmodels.sourceforge.net/)
* [SciPy](http://www.scipy.org/)
* [scikit-learn](http://scikit-learn.org/)
* [Jupyter](http://jupyter.org/)
* [matplotlib](http://matplotlib.org/)
* [tensorflow](https://www.tensorflow.org/)

Assorted:

* decorators
* coroutines yield pass await generators future
* scoping: global nonlocal
* multi-line strings
* named arguments
* range 1..10
* array slices[::]
* assert
* del
* with
* return
* versions: puthon2/3 implementations
* string/tuple/list slicing [start:end:stride]
* namedtuple https://docs.python.org/dev/library/collections.html#collections.namedtuple
* http://stackoverflow.com/questions/101268/hidden-features-of-python

Are there such features?

* destructing assignment/unpacking assignment // arguments

Research these topics:

* It's a Python convention to consider variables that start with an
  underscore to be private.
 * `vars(obj)` vs. `obj.__dict__` vs. `dir(obj)`: Syntax, local vars vs. inheritance chain; k/v vs. keys

## Data structures:

* general data structures (JSON: number, string, list, dict); 
* fine-grained data structures (list vs. tuple); 
* special-purpose extensions: numpy, pandas, tensorflow...
