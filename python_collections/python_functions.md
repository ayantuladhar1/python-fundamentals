# What is a Function?
* A function is a block of reusable code that runs only when called.

# Syntax:
```python
	def function_name(parameters):
	    statements
	    return value
```
# Basic Function Example:
```python
	def greet():
	    print("Hello, Welcome to Python")
	greet()
```
<img width="279" height="44" alt="image" src="https://github.com/user-attachments/assets/5698dd2e-0f56-49ab-988b-85d1c8ae2e73" />

# Function with Parameters:
```python
	def add_numbers(a, b):
	    return a + b
	result = add_numbers(10, 20)
	print(result)
```
<img width="36" height="38" alt="image" src="https://github.com/user-attachments/assets/5536384a-0675-4b6a-a742-e2a9f4147d88" />

# Function with Default Parameters:
```python
	def country(name="USA"):
	    print("Country is:", name)
	country()
	country("Nepal")
```
<img width="191" height="56" alt="image" src="https://github.com/user-attachments/assets/9b6ecaaf-2db3-43dd-bd98-8c58e2c8fa92" />

# Function Using If-Else:
```python
	def check_even_odd(num):
	    if num % 2 == 0:
	        return "Even"
	    else:
	        return "Odd"
	print(check_even_odd(10))
```
<img width="62" height="39" alt="image" src="https://github.com/user-attachments/assets/6ee23d1d-093d-4314-aa8e-2392342390ae" />

# Function Using List:
```python
	def total_marks(marks):
	    return sum(marks)
	marks = [80, 90, 85]
	print(total_marks(marks))
```
<img width="48" height="30" alt="image" src="https://github.com/user-attachments/assets/bc5d4c95-f205-4429-98dc-6098005996e1" />

