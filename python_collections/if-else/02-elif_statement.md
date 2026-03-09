# Elif Keyword
The elif keyword is Python's way of saying "if the presvios conditions were not ture, then try this condition".
The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.

## Example:
```python
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
```
<img width="155" height="30" alt="image" src="https://github.com/user-attachments/assets/fac7af84-9ac9-4495-9bb5-ba258880f91f" />

In this example a is equal to be, so the first condition is not ture, but the elif  condition is true, so we print to screen that "a and b are equal".

## Multiple Elif Statements
You can have as many elif statements as you need. Python will check each condition in order and execute the first one that is true.

## Example:
Testing mupltiple conditions:
```python
score = 75
if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
```
<img width="81" height="28" alt="image" src="https://github.com/user-attachments/assets/7a305281-7c81-43f1-ab71-f0871b043380" />

In this example, the program checks eacj condition in order. Since order is 75, it prints "Grade C" (the first condition that evaluates to true).

## How Elif Works
When you use elif, Python evauates the condtions from top to bottom. As soon as it finds a condition that is true, it executes that block and skips all the remaining conditions.
