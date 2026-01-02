# What is an Exception?
* An exception is an error that occurs during program execution.
* Exception handling prevents program crashes.

# Syntax:
```python
	try:
	    code that may cause error
	except:
	    code if error occurs
```
# Basic Try-Except:
```python
  try:
	    x = 10 / 0
	except:
	    print("Cannot divide by zero")
```
# Catch Specific Exception:
```python
  try:
	    x = int("abc")
	except ValueError:
	    print("Invalid conversion")
```
# Try-Except-Else:
```python
  try:
	    x = 10 / 2
	except:
	    print("Error occurred")
	else:
	    print("Result is:", x)
```
# Try-Except-Finally:
```python
  try:
	    file = open("data.txt")
	    print(file.read())
	except:
	    print("File not found")
	finally:
	    print("Execution completed")
```
# Exception Handling with User Input:
```python
  try:
	    num = int(input("Enter a number: "))
	    print(10 / num)
	except ZeroDivisionError:
	    print("Cannot divide by zero")
	except ValueError:
	    print("Enter only numbers")
```
