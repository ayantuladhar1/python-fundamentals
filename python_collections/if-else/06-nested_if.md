# Nested If Statements
You can have if statements inside if statements. This is called nested if statements.

## Example:
```python
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
```
<img width="193" height="66" alt="image" src="https://github.com/user-attachments/assets/53f7f283-dc7a-4d33-9bc0-08bd96fd692c" />

In this example, the inner if statement only runs if the outer condition (x > 10) is true.

## How Nested If Works
Each level of nesting creates a deeper level of decision-making. The code evaluates from the outermost condition inward.

## Example:
Checking multiple conditions with nesting:
```python
age = 25
has_license = True
if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")
```
<img width="201" height="40" alt="image" src="https://github.com/user-attachments/assets/1a63dc81-cd0e-43bb-940c-fc3809e1c247" />

## Multiple Levels of Nesting
You can nest as many levels deep as needed, but keep in mind that too many levels can make code harder to read.

## Example:
Three levels of nesting:
```python
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")
```
<img width="236" height="31" alt="image" src="https://github.com/user-attachments/assets/414f0f75-fa66-4f6d-9b05-02465756cd18" />

## Nested If vs Logical Operators
Sometimes nested if statements can be simplified using logical operators like and. The choice depends on your logic.

## Example:
This nested if:
```python
temperature = 25
is_sunny = True
if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")
```
<img width="230" height="39" alt="image" src="https://github.com/user-attachments/assets/40394147-03b5-463e-bf0e-7bcdb36b1958" />

## Example:
Could also be written with and:
```python
temperature = 25
is_sunny = True
if temperature > 20 and is_sunny:
  print("Perfect beach weather!")
```
<img width="234" height="37" alt="image" src="https://github.com/user-attachments/assets/5605be3f-c553-409a-9d76-958bc0b19e54" />

Both approaches produce the same result. Use nested if statements when the inner logic is complex or depends on the outer condition. Use and when both conditions are simple and equally important.

## More Examples:
Login validation with nested checks:
```python
username = "Emil"
password = "python123"
is_active = True
if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")
```
<img width="169" height="34" alt="image" src="https://github.com/user-attachments/assets/cfb61c91-ccc0-410f-ad80-ffb2a76daa05" />

## Example:
Grade calculation with nested logic:
```python
score = 92
extra_credit = 5
if score >= 90:
  if extra_credit > 0:
    print("A+ grade")
  else:
    print("A grade")
elif score >= 80:
  print("B grade")
else:
  print("C grade or below")
```
<img width="93" height="35" alt="image" src="https://github.com/user-attachments/assets/249f0eed-3fc4-4adb-88d7-0f58569c5aec" />
