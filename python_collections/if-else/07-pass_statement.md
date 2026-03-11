# Pass Statement
if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

## Example:
```python
a = 33
b = 200
if b > a:
  pass
# having an empty if statement like this, would raise an error without the pass statement
```
The pass statement is a null operation - nothing happends when it executes. It serves as a placeholder.

## Why Use pass?
The pass statement is useful in several sitautions:
* When you are creating code structure but haven't implemented the logic yet
* When a statement is required syntactically but no action is needed
* As a placeholder for future code during development
* In empty functions or classes that you plan to implement later

## Pass in Development
During development, you might want to sketch out your program structure before implementing the details. The pass statement allows you to do this without syntax errors.

## Example:
Placeholder for future implementation:
```python
age = 16
if age < 18:
  pass  # TODO: Add underage logic later
else:
  print("Access granted")
```
<img width="153" height="37" alt="image" src="https://github.com/user-attachments/assets/0bf26a5b-114f-4baa-bdd3-7ac32bc4f299" />

## Pass vs Comments
A comment is ignored by Python, but pass is an actual statement that getss executed (though it does nothing). You need pass where Python expects a statement, not just a comment.

## Example:
This will cause an error (empty code block):
```python
score = 85
if score > 90:
  # This is excellent
# This will raise an IndentationError
```

## Example:
This works correctly with pass:
```python
score = 85
if score > 90:
  pass  # This is excellent
print("Score processed")
```
<img width="165" height="37" alt="image" src="https://github.com/user-attachments/assets/656d0adc-20eb-434f-96dc-ca2d41a1c233" />

## Pass with Multiple Conditions
You can use pass in any branch of an if-elif-else statement.

## Example:
Using pass in different branches:
```python
value = 50
if value < 0:
  print("Negative value")
elif value == 0:
  pass  # Zero case - no action needed
else:
  print("Positive value")
```
<img width="153" height="29" alt="image" src="https://github.com/user-attachments/assets/279574c7-42ed-4a2f-ac3e-87a9f4b3005a" />

## Pass in Other Contexts
While we focus on pass with if statements here, it's also commonly used with loops, functions, and classes.

## Example:
Using pass with functions:
```python
def calculate_discount(price):
  pass  # TODO: Implement discount logic
# Function exists but doesn't do anything yet
```
