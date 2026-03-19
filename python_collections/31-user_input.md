# Python User Input
Pyhton allows for user input.
That means we are able to ask the user for input.
The following example asks for your name, and when you enter a name, and when you enter a name, it gets printed on the screen:

## Example:
Ask for user input:
```python
print("Enter your name:")
name = input()
print(f"Hello {name}")
```
<img width="189" height="95" alt="image" src="https://github.com/user-attachments/assets/eb51cb01-db37-4514-86ff-9122c6921173" />

Python stops the execution when it comes to the input() function, and continues when the user has given some input.

## Using prompt
In the example above, the user had to input their name on a new line. The Python input() function has a prompt parameter, which acts as a message you can put in front of the user input, on the same line:

## Example:
Add a message in front of the user input:
```python
name = input("Enter your name:")
print(f"Hello {name}")
```
<img width="214" height="57" alt="image" src="https://github.com/user-attachments/assets/b5493da4-5c69-4793-8dfd-2c6cf2a12401" />

## Multiple inputs
You can add as many inputs as you want, Python will stop executing at each of them, waiting for user input:

## Example:
Multiple inputs:
```python
name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite animal? ")
fav2 = input("What is your favorite color? ")
fav3 = input("What is your favorite number? ")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")
```
<img width="375" height="188" alt="image" src="https://github.com/user-attachments/assets/52b64793-8ed2-40af-b3ef-721de13a4d46" />

## Input Number
The input from the user is treated as a string. Even if, in the example above, you can input a number, the Python interpreter will still treat it as a string.
You can convert the input into a number with the float() function:

## Example:
To find the square root, the input has to be converted into a number:
```python
import math
x = input("Enter a number:")
#find the square root of the number:
y = math.sqrt(float(x))
print(f"The square root of {x} is {y}")
```
<img width="279" height="64" alt="image" src="https://github.com/user-attachments/assets/35e6e340-b48f-4490-acd0-e6bbaf7d0fd6" />

## Validate Input
It is a good practice to validate any input fromt the user. In the example above, an error will occur if the user inputs something other than a number.
To avoid getting an error, we can test the input, and if it is not a number, the user could get a message like "Wrong input, please try again," and allowed to make a new input:

## Example:
Keep asking until you get a number:
```python
y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x);
    y = False
  except:
    print("Wrong input, please try again.")
print("Thank you!")
```
<img width="314" height="176" alt="image" src="https://github.com/user-attachments/assets/394fc675-afee-4875-976b-dfa434b12d27" />
