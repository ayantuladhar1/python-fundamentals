# Logical Operators
Logical operators are used to combine conditional statements. Python has three logical operators:
* and - Returns True if bothe statements are true
* or - Returns True if one of the statements is true
* not - Reverses the result, return False if the result is true

## The and Operator
The and keuword is a logical operator and is used to combine conditional statements. Both conditions must be true for the entire expression to be true.

## Example:
Test if a is greater than b, AND if c is greater than a:
```python
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
```
<img width="263" height="30" alt="image" src="https://github.com/user-attachments/assets/26411d63-c22f-4e7e-baab-0af48f739d02" />

## The or Operator
The or keyword is a logical operator, and is used to combine conditional statements. At least one condition must be true for the entire expression to be true.

## Example:
Test if a is greater than b, OR if a is greater than c:
```python
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
```
<img width="396" height="30" alt="image" src="https://github.com/user-attachments/assets/ef7a312b-228a-4ea8-8b8e-333b0653b951" />

## The not Operator
The not keyword is a logical, and is used to reverse the result of the conditional statement.

## Example:
Test if a is NOT greater than b:
```python
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
```
<img width="248" height="46" alt="image" src="https://github.com/user-attachments/assets/8bde961c-9ced-4070-9dbf-5400ff45ba16" />

## Combining Multiple Operators
You can combine multiple logical operators in a single expression. Python evalutaes not first, then and, then or.

## Example:
Combining and, or, and not:
```python
age = 25
is_student = False
has_discount_code = True
if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")
```
<img width="182" height="41" alt="image" src="https://github.com/user-attachments/assets/bef0fd56-e07f-49f5-baad-e99b048c84de" />

## Truth Tables
Understanding how logical operators work with different values:

And Operator Truth Table
|Condition 1| Condition 2| Result|
|-----------|------------|-------|
|True| True| True|
|True| False| False|
|False| True| False|
|False| False| False|

OR Operator Truth Table
|Condition 1| Condition 2| Result|
|True| True| True|
|True| False| True|
|False| True| True|
|False| False| False|

## Using Parentheses for Clarity
When combining multiple logical operators, use parantheses to make your intentions clear and control the order of evaluation.

## Example:
Using parantheses for complex conditions:
```python
temperature = 25
is_raining = False
is_weekend = True
if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")
```
<img width="349" height="33" alt="image" src="https://github.com/user-attachments/assets/2cd2354f-05ed-4eb1-90eb-1fae4f1f7dd7" />

## More Examples
Use authentication check:
```python
username = "Tobias"
password = "secret123"
is_verified = True
if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")
```
<img width="172" height="37" alt="image" src="https://github.com/user-attachments/assets/29992eff-e718-48c0-954a-8dee4f9d7f3b" />

## Example:
Range checking with logical operators:
```python
score = 85
if score >= 0 and score <= 100:
  print("Valid score")
else:
  print("Invalid score")
```
<img width="121" height="39" alt="image" src="https://github.com/user-attachments/assets/d9fc255a-e7cf-4cf9-90b8-084d5f63b2c0" />
