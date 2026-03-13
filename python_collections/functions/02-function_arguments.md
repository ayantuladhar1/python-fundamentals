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

