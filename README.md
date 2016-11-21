# LearnPython

I already know scripting (Perl, JavaScript) that arguably have a lot in common with Python.

My first step is to explore what I *already know and understand:* Just learn the right syntax for
the pieces of Python that are shared with other languages.  In this step, I ignore features that
are different *on purpose:* They will be covered in the second step.

* [BabyPython](BabyPython.md): The language for basic algorithms
* [Generators](Generators.md): Generators: a lazy sequence of values
* [Async](Async.md): Async functions for efficient parallel communication

Topics to cover here:

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

References:
* [Tutorial](https://docs.python.org/3/tutorial/)
* [Numpy tutorial](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html)
* [Language reference](https://docs.python.org/3/reference/index.html)
* [Library reference](https://docs.python.org/3/library/)
* [Style guide](https://www.python.org/dev/peps/pep-0008/)

