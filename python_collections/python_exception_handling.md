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
<img width="239" height="35" alt="image" src="https://github.com/user-attachments/assets/2902510d-c335-4a41-b034-179531e2c429" />

# Catch Specific Exception:
```python
  try:
	    x = int("abc")
	except ValueError:
	    print("Invalid conversion")
```
<img width="208" height="38" alt="image" src="https://github.com/user-attachments/assets/3666c330-3e25-42c5-b2ce-02bb6971a333" />

# Try-Except-Else:
```python
  try:
	    x = 10 / 2
	except:
	    print("Error occurred")
	else:
	    print("Result is:", x)
```
<img width="162" height="27" alt="image" src="https://github.com/user-attachments/assets/95b8488d-b6ed-455e-8e62-abeb2efe0b19" />

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
<img width="209" height="52" alt="image" src="https://github.com/user-attachments/assets/48330cba-4b51-4a2f-a139-43216501f231" />

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
<img width="246" height="54" alt="image" src="https://github.com/user-attachments/assets/910f33f5-395f-4d41-895e-4f980f91dd33" />

