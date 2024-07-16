Functions are named sections of a program that are written to preform a specific task. Functions are the cornerstone of modular programming. Utilizing them correctly allows for clean, fast, recourse efficient code. 

Functions usually take an input, do work on it, and return output. There are four main types of functions:

1. Built-in functions
2. User-defined functions
3. Anonymous functions
4. Higher-order functions

Built-in functions are included with the programming language. The purpose of them is to make the process of writing code in that language easier. An example is the `print()` function included in the Python SDK or `Console.WriteLine()` in C#.

User-defined functions are written by the programmer for specific use cases. An example of a user-defined function would be:

```
def get_sum(a, b):
    return (a + b)
```

An anonymous function is one that can be immediately invoked or stored in a variable. They are also called lambda functions. They are most often used when they are only needed once, or will not be called by anything else in the program. An example of an anonymous (lambda) function is:

```
add_numbers = lambda a,b : a + b
print(add_numbers(2,3))
```

Higher-order functions are functions that either contain other functions as parameters or returns a function as an output. Examples of functions being passed and returned are:

Passing functions:
```

def shout(text): 
    return text.upper() 
  
def whisper(text): 
    return text.lower() 
  
def greet(func): 
    # storing the passed function in a scoped variable 
    greeting = func("Hello world.") 
    print(greeting)  
  
greet(shout) 
greet(whisper)
```

Returning functions:
```
def create_adder(x): 
    def adder(y): 
        return x + y 
  
    return adder 
  
add_15 = create_adder(15) 
  
print(add_15(10))
```