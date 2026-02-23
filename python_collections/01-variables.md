# Variables  
```python
x = 5
y = "John"
print(x)
print(y)
```
<img width="65" height="57" alt="image" src="https://github.com/user-attachments/assets/192f0b40-f5a4-4106-900b-fb14fe423159" />

# Casting  
If you want to specify the data type of a variable, this can be done with casting.  
```python
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
```
<img width="73" height="75" alt="image" src="https://github.com/user-attachments/assets/b332c6e1-4409-4c8f-bdb8-55ab29b0f037" />

# Get the Type  
```python
x = 5
y = "John"
print(type(x))
print(type(y))
```
<img width="154" height="49" alt="image" src="https://github.com/user-attachments/assets/0f098420-49ab-4657-aae1-64aa5841fef1" />

# Single or Double Quotes?  
```python
x = "John"
# is the same as
x = 'John'
```
<img width="61" height="35" alt="image" src="https://github.com/user-attachments/assets/a5e2424d-3ad9-45f8-8b54-9d97aced6ea3" />

# Case-Sensitive  
Variable names are case-sensitive.  
```python
a = 4
A = "Sally"
#A will not overwrite a
```

# Many Values to Multiple Variables
```python
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
```
<img width="82" height="85" alt="image" src="https://github.com/user-attachments/assets/9cf4b594-7e99-492c-b542-9b5c29fdc831" />

# One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:
```python
x = y = z = "Orange"
print(x)
print(y)
print(z)
```
<img width="84" height="67" alt="image" src="https://github.com/user-attachments/assets/b360512f-5261-4608-b0cc-1a6f09b0a28c" />

# Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking
```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
```
<img width="76" height="74" alt="image" src="https://github.com/user-attachments/assets/7fb7499d-e556-46bc-bc3f-1deb1dd93529" />

# Output Variables
The Python print() function is often used to output variables.
```python
x = "Python is awesome"
print(x)
```
<img width="185" height="29" alt="image" src="https://github.com/user-attachments/assets/70e37a18-1270-407e-998c-c0059b3ea590" />

# In the print() function, you output multiple variables, separated by a comma:
The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
```python
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
```
<img width="190" height="37" alt="image" src="https://github.com/user-attachments/assets/9145c68c-be22-4664-b45f-47948ee4afb7" />

# Global Variables
Variables that are created outside of a function (as in all of the examples above) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
```python
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()
```
<img width="187" height="32" alt="image" src="https://github.com/user-attachments/assets/6fd26610-0398-49e0-94ac-4d4a3cd49f27" />

