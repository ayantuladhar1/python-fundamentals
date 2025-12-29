#Variables  
```python
x = 5
y = "John"
print(x)
print(y)
```

#Casting  
If you want to specify the data type of a variable, this can be done with casting.  
```python
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
```

#Get the Type  
```python
x = 5
y = "John"
print(type(x))
print(type(y))
```

#Single or Double Quotes?  
```python
x = "John"
# is the same as
x = 'John'
```

#Case-Sensitive  
Variable names are case-sensitive.  
```python
a = 4
A = "Sally"
#A will not overwrite a
```

#Many Values to Multiple Variables
```python
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
```

#One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:
```python
x = y = z = "Orange"
print(x)
print(y)
print(z)
```

#Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking
```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
```

#Output Variables
The Python print() function is often used to output variables.
```python
x = "Python is awesome"
print(x)
```

#In the print() function, you output multiple variables, separated by a comma:
The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
```python
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
```

#Global Variables
Variables that are created outside of a function (as in all of the examples above) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"

def myfunc():
  print("Python is " + x)
myfunc()
