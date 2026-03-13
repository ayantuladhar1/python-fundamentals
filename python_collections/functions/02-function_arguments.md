# Python Function Arguments
Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parantheses. You can add as many arguments as you want, just separate them with comma.
The following example has a function with one argument(fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

## Example:
A function with one argument:
```python
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")
```
<img width="135" height="73" alt="image" src="https://github.com/user-attachments/assets/9d9eb17c-d45f-4fb3-9e3b-a1d8d95737cf" />

## Parameter vs Arguments
The terms parameter and argument can be used for the same thing: information that are passed into a function.
From a function's perspective:
A parameter is the variable listed inside the parantheses in the function definition.
An argument is the actual value that is sent to the function when it is called.

## Example:
```python
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument
```

## Number of Arguments
By default, a function must be called with the correct number of arguments.
If your function expects 2 arguments, you must call it with 2 arguments.

## Example:
This function expects 2 arguments, and gets 2 arguments:
```pyhton
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")
```
<img width="115" height="30" alt="image" src="https://github.com/user-attachments/assets/f1302c55-2e5f-4fdf-a4ff-9fc754f36671" />

If you try to call the function with the wrong number of arguments, you will get an error:
```python
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil")
```
<img width="649" height="108" alt="image" src="https://github.com/user-attachments/assets/0fbd776c-aa50-4df7-9cc4-4e8a254afe9b" />

## Default Parameter Values
You can assign default values to parameters. If the function is called without an argument, it uses the default values:

## Example:
```python
def my_function(name = "friend"):
  print("Hello", name)
my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")
```
<img width="115" height="96" alt="image" src="https://github.com/user-attachments/assets/5dc35e9a-6e60-4177-8ac8-cd2be7062539" />

## Example:
Default value for country parameter:
```python
def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
```
<img width="159" height="107" alt="image" src="https://github.com/user-attachments/assets/6fbcf0e7-4e65-4fc1-bbfb-728483c18a99" />

## Keyword Arguments
You can send argumnets with key = value syntax

## Example:
```python
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function(animal = "dog", name = "Buddy")
```
<img width="206" height="52" alt="image" src="https://github.com/user-attachments/assets/f7ddc615-6334-4ae1-9bbe-3c04c3bfb027" />

This way, with keyword arguments, the order of the arguments does not matter.

## Example:
```python
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function(name = "Buddy", animal = "dog")
```
<img width="204" height="52" alt="image" src="https://github.com/user-attachments/assets/5e4e8b35-1d0e-4c13-9272-a619c6029a09" />

The phrase Keyword Arguments is often shortened to kwargs in Python documentation.

## Position Arguments
When you call a function with argumnets without using keywords, they are called positional arguments.
Position arguments must be in the correct order.

## Example:
```python
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function("dog", "Buddy")
```
<img width="212" height="60" alt="image" src="https://github.com/user-attachments/assets/4a167fa1-d21c-49b6-a2d3-a4a2bfbff62c" />

The order matters with positional arguments:

## Example:
Switching the order changes the result:
```python
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function("Buddy", "dog")
```
<img width="207" height="56" alt="image" src="https://github.com/user-attachments/assets/94827136-3238-475a-a6e5-8b8e7f79ba7e" />

## Mixing Positional and Keyword Arguments
You can mix positional and keyword arguments in a function call.
However, positional arguments must come before keyword arguments:

## Example:
```python
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)
my_function("dog", name = "Buddy", age = 5)
```
<img width="314" height="30" alt="image" src="https://github.com/user-attachments/assets/e869ff48-191c-411c-9252-8fa3a62a63e6" />

## Passing Different Data Types
You can send any data type as an argument to a function (string, number, list, dictionary), etc.
The data type will be preserved inside the fucntion:

## Example:
Sending a list as an argument:
```python
def my_function(fruits):
  for fruit in fruits:
    print(fruit)
my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)
```
<img width="69" height="77" alt="image" src="https://github.com/user-attachments/assets/7aa413a3-217d-45e2-b749-f88bb9e5e401" />

## Example:
Sending a dictionary as an argument:
```python
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])
my_person = {"name": "Emil", "age": 25}
my_function(my_person)
```
<img width="105" height="51" alt="image" src="https://github.com/user-attachments/assets/5cc6399d-b022-40e0-a0d6-030e5cdcdf7c" />

## Return Values
Functions can return values using the return statement:

## Example:
```python
def my_function(x, y):
  return x + y
result = my_function(5, 3)
print(result)
```
<img width="18" height="29" alt="image" src="https://github.com/user-attachments/assets/7ab885b7-7819-4eb1-bb0d-ec6a01e2d6d3" />

## Returning Different Data Types
Functions can return any data type, including list, tuples,dictionaries, and more.

## Example:
A function that returns a list:
```python
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])
```
<img width="72" height="76" alt="image" src="https://github.com/user-attachments/assets/064f58b0-b076-428d-81f2-4340732533e0" />

## Example:
A function that returns a tuple:
```python
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)
```
<img width="57" height="55" alt="image" src="https://github.com/user-attachments/assets/bef18228-5e3f-4523-9719-b3b9b2f5eccf" />

## Positional-Only Arguments
You can specify that a function can have ONLY positional arguments.
To sepcify positional-only arguments, add "/" afterthe arguments:

## Example:
```python
def my_function(name, /):
  print("Hello", name)
my_function("Emil")
```
<img width="99" height="30" alt="image" src="https://github.com/user-attachments/assets/60bbff30-c70c-48c3-bf95-045964f58a9c" />

Without the "/" you are actually allowed to use keyword arguments even if the function expects positional arguments:

## Example:
```python
def my_function(name):
  print("Hello", name)
my_function(name = "Emil")
```
<img width="92" height="30" alt="image" src="https://github.com/user-attachments/assets/b0c8f6fb-99a1-4423-a7f6-6b2b8ea06b4d" />

With "/" you will get an error if you try to use keyword arguments:

## Example:
```python
def my_function(name, /):
  print("Hello", name)
#This will cause an error:
my_function(name = "Emil")
```
<img width="677" height="75" alt="image" src="https://github.com/user-attachments/assets/7ca7632f-088b-46a4-9559-7eb9533eb469" />

## Keyword-Only Arguments
To specify that a function can have only keyword arguments, add "*" before the arguments:

## Example:
```python
def my_function(*, name):
  print("Hello", name)
my_function(name = "Emil")
```
<img width="96" height="23" alt="image" src="https://github.com/user-attachments/assets/da96adac-55b0-42ea-b395-1c2cebddc3c4" />

Without "*" you are allowed to use positional arguments even if the function expects keyword arguments:

## Example:
```python
def my_function(name):
  print("Hello", name)
my_function("Emil")
```
<img width="92" height="26" alt="image" src="https://github.com/user-attachments/assets/3f2824c7-bd9b-4c9c-91ec-655685b8ce7d" />

With "*" you will get an error if you try to use positional arguments:

## Example:
```python
def my_function(*, name):
  print("Hello", name)
my_function("Emil")
```
<img width="624" height="81" alt="image" src="https://github.com/user-attachments/assets/a948d06d-1ffe-4f36-8916-c5922eeb9838" />

## Combining Positional-Only and Keyword-Only
You can combine both argument types in the same function.
Arguments before "/" are positional-only and arguments after "*" are keyword only:

## Example:
```python
def my_function(a, b, /, *, c, d):
  return a + b + c + d
result = my_function(5, 10, c = 15, d = 20)
print(result)
```
<img width="31" height="23" alt="image" src="https://github.com/user-attachments/assets/c5e30b02-db6e-44d5-b92b-41a301ebe973" />
