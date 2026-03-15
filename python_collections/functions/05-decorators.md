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

