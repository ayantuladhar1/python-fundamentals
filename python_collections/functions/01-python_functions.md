# Python Functions
A function is a block of code which only runs when it is called.
A function can return data as a result.
A function helps avoiding code replication.

## Creating a Function
In Python, a function is defined using the def keyword, followed by a function name and parantheses:

## Example:
```python
def my_function():
  print("Hello from a function")
```
This creates a function named my_function that prints "Hello from a function" when called.

The code inside the function must be indented. Python uses identation to define code blocks.

## Calling a Function
To call a function, write its name followed by parantheses:

## Example:
```python
def my_function():
  print("Hello from a function")
my_function()
```
<img width="189" height="33" alt="image" src="https://github.com/user-attachments/assets/ce703d00-b651-4115-822f-3f4795988e82" />

You can call the same function multiple times:

## Example:
```python
def my_function():
  print("Hello from a function")
my_function()
my_function()
my_function()
```
<img width="199" height="78" alt="image" src="https://github.com/user-attachments/assets/dbd6ca32-2350-4499-873c-530ec211d778" />

## Function Names
Function names follow the same rules as variable names in Python:
* A function name must start with a letter or underscore
* A function name can only contain letters, number, and underscores
* Function names are case-sensitive (myFunction and myfunction are different)

## Example:
Valid function names:
```python
calculate_sum()
_private_function()
myFunction2()
```

It's a good practice to use descriptive names that explain what the function does.

## Why Use Functions?
Imaging you need to convert temperatures from Farenheit to Celsius several times in your program. Without functions, you would have to write the same calculation code repreatedly:

## Example
Without functions - repetitive code:
```python
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)
```
<img width="48" height="72" alt="image" src="https://github.com/user-attachments/assets/ac698b9f-13c9-4a21-b659-2e6f898b7ee2" />

With functions, you write the code once and reuse it.

## Example:
With functions - resuable code:
```python
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))
```
<img width="44" height="78" alt="image" src="https://github.com/user-attachments/assets/1415f473-9162-4576-bcac-4b1919aff893" />

## Return Values
Function can send data to the code that called them using the return statement.
When a function reaches a return statement, it stops executing and sends the result back:

## Example:
A function that returns a value:
```python
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)
```
<img width="198" height="29" alt="image" src="https://github.com/user-attachments/assets/89788335-877b-4e7d-a3d8-18f2470dfe0c" />

You can use the returned value directly:

## Example
Uisng the return value directly:
```python
def get_greeting():
  return "Hello from a function"
print(get_greeting())
```
<img width="196" height="36" alt="image" src="https://github.com/user-attachments/assets/d95cf50f-cabe-4bc9-8f0b-f9314a45b6fb" />

If a functuion doesn't have a return statement, it returns None by default.

## The Pass Statement
Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:

## Example:
```python
def my_function():
  pass
```
The pass statement is often used when developing, allowing you to deffine the structure first and implement details later.
