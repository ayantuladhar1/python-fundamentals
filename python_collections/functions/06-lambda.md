# Python Lambda
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

##  Syntax
```python
lambda arguments : expression
```
The expression is executed and the result is returned:

## Example:
Add 10 to argument a, and return the result
```python
x = lambda a: a + 10
print(x(5))
```

## Output
15

Lambda function can take any number of arguments:

## Example:
Multiply argument a with argument b and return the result:
```python
x = lambda a, b: a * b
print(x(5, 6))
```

## Output
30

## Example:
Summarize argument a, b, and c and return the result:
```python
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))
```

## Output
13

## Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous functions inside another function.
Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
```python
def myfunc(n):
  return lambda a : a * n
```
Use that function definition to make a function that always doubles the number you send in:

## Example:
```python
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
```

## Output
22

Or, use the same function definition to make a function that always triples the number you send in:

## Example:
```python
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)
print(mytripler(11))
```

## Output
33

Or, use the same function definition to make both functions, in the same program:

## Example:
```python
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))
```

## Output
22
33

Use lambda function when an anonymous function is required for a short period of time.

## Lambda with Built-in Functions
Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().

## Using Lambda with map()
The map() function applied a fucntion to every time in an iterable:

## Example:
Double all numbers in a list:
```python
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
```

## Output
```list
[2, 4, 6, 8, 10]
```
