# Python Decorators
Decorators let you add extra behavior to a function, without changing the function's code.
A decorator is a function that takes another function as input and returns a new function.

## Basic Decorators
Define the decorator first, then apply it with @decorator_name above the function.

## Example:
A basic decorator that uppercases the return value of the decorated function.
```python
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"
print(myfunction())
```

## Output
HELLO SALLY

By placing @changecase directly above the function definition, the function myfunction is being "decorated" with the changecase function.
The function changecase is the decorator.
The function myfunction is the function that gets decorated.

## Multiple Decorator Calls
A decorator can be called multiple times. Just place the decorator above the function you want to decorate.

## Example:
Using the @changecase decorator on two functions:
```python
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())
```

## Output
HELLO SALLY  
I AM SPEED!  

## Arguments in the Decorated Function
Function that requires arguments can also be decorated, just make sure you pass the arguments to the wrapper function:

## Example:
Functions with arguments can also be decorated:
```python
def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam
print(myfunction("John"))
```

## Output
HELLO JOHN

## *args and **kwargs
Sometimes the decorator function has no control over the arguments passed from the decorated functions, to solve this problem, add (*args, **kwargs) to the wrapper function, this way the wrapper fcuntion can accept any number,and any type of arguments, and pass them to the decorated function.

## Example:
Secure the function with *args and **kwargs arguments:
```python
def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam
print(myfunction("John"))
```

## Output
HELLO JOHN

## Decorators with Arguments
Decorators can accept their own arguments by adding another wrapper level.

## Example:
A decorator factory that takes an argument and transforms the casing based on the argument value.
```python
def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"
print(myfunction())
```

## Output
hello linus

## Multiple Decorators
You can use multiple decorators on one function.
This is done by placing the decorator calls on top of each other.
Decorators are called in the reverse order, starting with the one closest to the function.

## Example:
One decorator for upper case, and one for adding a greeting:
```python
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"
print(myfunction())
```

## Output
HELLO TOBIAS HAVE A GOOD DAY!

## Preserving Function Metadata
Functions in Python has metadata that can be accessed uwing the __name__ and __doc__ attributes.

## Example:
Normally, a function's name can be returned with the __name__ attribute:
```python
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)
```

## Output
myfunction

But when a function is decorated the metadata of the original function is lost.

## Example:
Try returning the name from a decorated function and you will not get the same result:
```python
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"
print(myfunction.__name__)
```

## Output
myinner

To fix this, Python has a built-in function called functools.wraps that can be used to preserve the original function's name and docstring.

## Example:
Import functools.wraps to preserve the original function name and docstring.
```python
import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)
```

## Output
myfunction
