# Baby Python
*The syntax for what you already know from other languages.*

## Hello world
*The `print` function needs brackets and automatically adds a newline character.*

    print("Hello world.")

*Execute a script by passing it to `python3`:*

    echo 'print("Hello world.")' > hello.py
    python3 hello.py
    
## Many statements; semicolons
*No semicolon is needed at the end of a line.*

    print("Hello world.")
    print("Hello..."); print("...world.")
    
## Control statements: for while if -- elif else

    for i in range(3):
        print(i)  # 0 1 2
    
    i=0  # Create a variable by assigning to it.
    while i<3:
        print i   # 0 1 2
        i=i+1
      
    if 2<10:
        print("Ok.")
    elif "2">"10":
        print("String comparison.")
    else:
        print("Not ok.")


## Scope and variable declaration
* Declare a variable by assigning to it.
* Blocks don't create new scope, functions do.

## JSON-like data: numbers, strings, lists, dicts

    data=[1, "hello", 'world', {'key': 'value'}]
    print(data[3]['key'])
    
    # variable keys in dict literals
    key='hello'; data={key: 'world'}
    print(data['hello'])  # world

## Expressions, function and method calls: no surprises
*Within brackets, you can break lines*

    import math
    print(math.pi)           # 3.141592653589793
    print(math.factorial(5)) # 1*2*3*4*5=120
    print(min(11,2));        # 2
    print(10 + 2*3)          # 16

    print(
        1 + 2*3
          - 4*5
          + 6*7
    )                        # 29
    
## Function definitions

    def factorial(n):
        product=1
        for factor in range(1,n+1): product *= factor
        return product
    
    print(factorial(5))      # 1*2*3*4*5=120

## Define a module
*This is factorial.py: top-level names will be exported.*
  
    def recursive(n):
        if n==0: return 1
        else:    return n*recursive(n-1)
        
    def loop(n):
        product=1
        for factor in range(1,n+1): product *= factor
        return product


## Use a module

    import factorial
    
    print(factorial.recursive(5))  # 120
    print(factorial.loop(5))       # 120
    
    from factorial import recursive, loop
    
    print(recursive(5))  # 120
    print(loop(5))       # 120
