# If Statement
## Python Condition and If Statements
Python supports the usual logical conditions from mathematics:
* Equals: a == b
* Not Equals: a != b
* Less Than: a < b
* Less Than or Equal To: a <= b
* Greater than: a > b
* Greter than or equal to: a >= b

These conditions can be used in several ways, most commonly in "if statements" and loops.
An "if statement" is written by using if keyword.

## Example:
If Statement:
```python
a = 33
b = 200
if b > a:
  print("b is greater than a")
```

In this example, we use two varialbles, a and b, which are used a part of the if statement to test whether b is greater than a. As a is 33, and b is 200, we know that 200 is greater than 33, and so we print to screen that "b is greater than a".

## How If Statement Work
The if statement evaluates a condition (an expression that results in True or False). If the condition is true, the code block inside the if statement is executed. If the condition is false, the code block is skipped.

## Example:
Checking if a number is positive:
```python
number = 15
if number > 0:
  print("The number is positive")
```

## Indentation
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

## Example:
If Statement, without indentation (will raise an error):
```python
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
```
<img width="413" height="110" alt="image" src="https://github.com/user-attachments/assets/8a5ac965-40e7-4880-8dc3-0325597b9d9e" />

## Multiple Statements in If Block:
You can have multiple statements inside an if block. All statements must be indented at the same level.

## Example:
Multiple statements in an if block:
```python
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")
```
<img width="243" height="81" alt="image" src="https://github.com/user-attachments/assets/5fbb794d-6692-4dad-941a-c3b3a22153be" />

## Using Variables in Conditions
Boolean variables can be used directly in if statements without comparison operators.

## Example:
```python
is_logged_in = True
if is_logged_in:
  print("Welcome back!")
```
<img width="127" height="33" alt="image" src="https://github.com/user-attachments/assets/2633d362-dd33-4de9-bdcd-29ce449c9833" />

Python can evaluate many types of values as True of False in an if statement.
Zero(0), empty strings(""), None, and empty collections are treated as False.
Everything else is treated as True.
This includes positive numbers(5), negative numbers (-3), and any non-empty string (even "False" is treated as True because it's a non-empty string).
