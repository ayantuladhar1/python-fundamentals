# Python Math
Python has a  set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.

## Built-in Math Functions
The min() and max() functions can be used to find the lowest or highest value in an iterable:

## Example:
```python
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)
```
<img width="25" height="54" alt="image" src="https://github.com/user-attachments/assets/59133d9a-b27d-4ad5-9f6b-4c5b0147ab0a" />

The abs() function returns the absolute(positive) value of the specified number:

## Example:
```python
x = abs(-7.25)
print(x)
```
<img width="48" height="28" alt="image" src="https://github.com/user-attachments/assets/7919ce65-faef-4819-8367-64b8efde1957" />

The pow(x, y) function returns the value of x to the power of y (x^y).

## Example:
Return the value of 4 to the power of 3 (same as 4 * 4 * 4):
```python
x = pow(4, 3)
print(x)
```
<img width="25" height="25" alt="image" src="https://github.com/user-attachments/assets/00659907-870c-438a-b394-1456822ae685" />

## The Math Module
Python has also a built-in module called math, which extends the list of mathematical functions.
To use it, you must import the math module:
```python
import math
```
When you have imported the math module, you can start using methods and constants of the module.
The math.sqrt() method for example, returns the square root of a number:

## Example:
```python
import math
x = math.sqrt(64)
print(x)
```
<img width="30" height="35" alt="image" src="https://github.com/user-attachments/assets/62cf26bf-d21a-4835-a0e4-66dbac324a30" />

The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:

## Example:
```python
#Import math library
import math
#Round a number upward to its nearest integer
x = math.ceil(1.4)
#Round a number downward to its nearest integer
y = math.floor(1.4)
print(x)
print(y)
```
<img width="18" height="51" alt="image" src="https://github.com/user-attachments/assets/81a051fe-3742-4fa1-b207-c748c99d6f3c" />

The math.pi constant, returns the value of PI(3.14...):

## Example:
```python
import math
x = math.pi
print(x)
```
<img width="157" height="29" alt="image" src="https://github.com/user-attachments/assets/6a28b006-b2ed-4609-915e-4e0375cff23c" />
