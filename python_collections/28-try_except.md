# Python Try Except
The try block lets you test a block of code for errors.
THe except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try and except blocks.

## Exception Handling
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
These exceptions can be handled using the try statement:

## Example:
The try block wil generate an exception, because x is not defined:
```python
#The try block will generate an error, because x is not defined:
try:
  print(x)
except:
  print("An exception occurred")
```
<img width="197" height="38" alt="image" src="https://github.com/user-attachments/assets/67244f5f-90f0-49f5-bad1-dceaae1e62e3" />

Since the try block raises an error, the except block will be executed.
Without the try block, the program will crash and raise an error:

## Example:
This statement will raise an error because x is not defined:
```python
#This will raise an exception, because x is not defined:
print(x)
```
<img width="481" height="116" alt="image" src="https://github.com/user-attachments/assets/ccc47804-2009-45f1-b7cd-5f0ff1395aa2" />

## Many Exceptions
You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for special kind of error:
Print one message if the try block raises a NameError and another for other errors:
```python
#The try block will generate a NameError, because x is not defined:
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
```
<img width="237" height="32" alt="image" src="https://github.com/user-attachments/assets/3122167e-cac4-46a8-9d14-a9dcd371ba87" />

## Else 
You can use the else keyword to define a block of code to be execute if no errors were raised:

## Example:
In this example, the try block does not guarante any error:
```python
#The try block does not raise any errors, so the else block is executed:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
```
<img width="179" height="62" alt="image" src="https://github.com/user-attachments/assets/2326d128-4170-472a-a0b8-4ed72d601154" />

## Finally
The finally block, if specified, will be executed regardless if the try block raises an error or not.

## Example:
```python
#The finally block gets executed no matter if the try block raises any errors or not:
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
```
<img width="253" height="54" alt="image" src="https://github.com/user-attachments/assets/47982353-8daa-4d2b-ada2-e80b756a346c" />

This can be used to close objects and clean up resources:

## Example:
Try to open and write to a file that is not writable:
```python
#The try block will raise an error when trying to write to a read-only file:
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  
```
<img width="408" height="32" alt="image" src="https://github.com/user-attachments/assets/d6055077-9baa-4f29-b44f-5af9c230225b" />

The program can continue, without leaving the file object open.

## Raise an exception
As a Python developer you can choose to throw an exception if a condition occurs.
To throw (or raise) and exception, use the raise keyword.

## Example:
Raise an error and stop the program if x is lower than 0:
```python
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")
```
<img width="492" height="95" alt="image" src="https://github.com/user-attachments/assets/e149fb93-004e-43dd-aaef-7b4e0a9a7d07" />

The raise keyword is used to raise an exception.
You can define what kind of error to raise, and the text to print to the user.

## Example:
Raise a TypeError if x is not an integer:
```python
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")
```
<img width="502" height="99" alt="image" src="https://github.com/user-attachments/assets/95964ded-dc2d-4c37-819c-d55b6d69c076" />

