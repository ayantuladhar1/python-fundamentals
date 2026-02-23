# A lambda function is a small anonymous function.
* A lambda function can take any number of arguments, but can only have one expression.

# Add 10 to argument a, and return the result
```python
x = lambda a : a + 10
print(x(5))
```
<img width="36" height="21" alt="image" src="https://github.com/user-attachments/assets/7947a3da-edbf-419c-85a9-a2f4a010d772" />

# Multiply argument a with argument b and return the result
```python
x = lambda a, b : a * b
print(x(5, 6))
```
<img width="32" height="26" alt="image" src="https://github.com/user-attachments/assets/391bc469-7b12-4539-95d8-d7ca07d390d3" />

# Summarise argument a, b, and c and return the result
```python
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
```
<img width="36" height="47" alt="image" src="https://github.com/user-attachments/assets/9ad97948-d6c6-456a-850e-227e5aa85c89" />

# The power of lambda is better shown when you use them as an anonymous function inside another function
* Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
```python
def myfunc(n):
  return lambda a : a * n

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
```
<img width="34" height="75" alt="image" src="https://github.com/user-attachments/assets/c6e160b0-9754-4083-b405-f88935326b67" />


