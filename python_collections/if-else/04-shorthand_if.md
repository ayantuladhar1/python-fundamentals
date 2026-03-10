# Shorthand If
If you only have one statement to execute, you can put it on the same line as the if statement.

## Example:
One-line if statement:
```python
a = 200
b = 33
if a > b: print("a is greater than b")
```
<img width="204" height="35" alt="image" src="https://github.com/user-attachments/assets/c9ed4750-9a92-42ac-a43b-e91ae5fed011" />

Note: You still need the colon : after the condition.

## Short Hand If...Else
If you have one statement for if and one for else, you can put them on the same line using a conditional expression:

## Example:
One-line if/else that prints a value:
```python
a = 2
b = 330
print("A") if a > b else print("B")
```
<img width="28" height="40" alt="image" src="https://github.com/user-attachments/assets/d1f3f61f-1726-427b-840d-4e3d95b326ea" />

This is called a conditional expresssion (sometimes known as a "ternary operator").

## Assign a Value With If...Elase

You can also use a one-line if/else to choose a value and assign it to a variable:

## Example:
```python
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)
```
<img width="137" height="40" alt="image" src="https://github.com/user-attachments/assets/d3a9f5ab-d69c-404d-8711-5160c2ebe141" />

The syntax follows this pattern:

variable = value_if_true if condition else value_if_false

## Multiple Conditions on One Line
You can chain conditional expressions, but keep it short so it stays readable:

## Example:
One line, three outccomes:
```python
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
```
<img width="23" height="32" alt="image" src="https://github.com/user-attachments/assets/2b89b3fb-6e18-440d-89c5-d676a38d7849" />

## Practical Examples
Ternary operatos are particularly useful for simple assignments and returns statements.

## Example:
Finding the maximum of two numbers:
```python
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)
```
<img width="188" height="25" alt="image" src="https://github.com/user-attachments/assets/11a0f366-e106-487c-b2d0-d00810079159" />

## Example:
Setting a default value:
```python
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)
```
<img width="153" height="29" alt="image" src="https://github.com/user-attachments/assets/24e7fef6-6147-484c-8d04-ed05187adc16" />

## When to Use Shorthand If
Shorthand if statement and ternary operators should be used when:
* The condition and actions are simple
* It improves code readability
* You want to make a quick assignment based on a condition

Important: While shorthand if statements can make code more concise, avoid overusing then for complex conditions.
For readability, use regular if-else statements when dealing with multiple lines of code or complex logic.
