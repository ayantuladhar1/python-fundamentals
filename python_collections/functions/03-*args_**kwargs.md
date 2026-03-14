# Python *args and ** kwargs
By default, a function must be called with the correct number of arguments.
However, sometimes you may not know how many arguments that will passed into your function.
*args and **kwargs allow function to accept a unknown number of arguments.

## Arbitary Arguments - *args
If you do not know how many arguments will be passed into your function, add a * before the parameter name.
This way, the function will receive a tuple of arguments and can access the items accordingly.

## Example:
Using *args to accept any number of arguments:
```python
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
```

## Output
The youngest child is Linus

## What is *args?
The *args parameter allows a function to accept any number of positional arguments.
Inside the function, args becomes a tuple containing all the passed arguments:

## Example:
Accessing individual arguments from *args:
```python
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")
```

## Output
Type: <class 'tuple'>
First argument: Emil
Second argument: Tobias
All arguments: ('Emil', 'Tobias', 'Linus')

## Using *args with Regular Arguments
You can combine regular parameters with *args.
Regular parameters must come before *args:

## Example:
```python
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)
my_function("Hello", "Emil", "Tobias", "Linus")
```

## Output
Hello Emil
Hello Tobias
Hello Linus

In this example, "Hello" is assigned to greeting, and the rest are collected in names.

## Practical Example with *args
*args is useful when you create flexible functions:

## Example:
A function that calculated the sume of any number of values:
```python
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))
```

## Output
6
100
5

## Example:
Fincing the maximum value:
```python
def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1))
```

## Output
9

## Arbitary Keyword Arguments - **kwargs
If you do not know how many keyword arguments will be passeed into your function, add two asterisks ** before the parameter name.
This way, the function will receive a dictionary of arguments and can access the items accordingly:

## Example:
Using **kwargs to accept any number of keyword arguments:
```python
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
```

## Output
His last name is Refsnes

Arbitary Keyword Arguments are often shortened to **kwargs in Python documentation.

## What is **kwargs?
The **kwargs 
