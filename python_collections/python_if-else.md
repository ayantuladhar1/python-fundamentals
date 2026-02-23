# Python Conditions and If statements  
Python supports the usual logical conditions from mathematics:  
* Equals: a == b
* Not Equals: a != b
* Less than: a < b
* Less than or equal to: a <= b
* Greater than: a > b
* Greater than or equal to: a >= b

```python
a = 33
b = 200
if b > a:
  print("b is greater than a")
```
<img width="210" height="27" alt="image" src="https://github.com/user-attachments/assets/3ca759f0-518d-4755-b684-594f9b332d5b" />

# Elif  
The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".  
```python
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
```
<img width="187" height="16" alt="image" src="https://github.com/user-attachments/assets/f92fc44c-02af-4311-b897-0a935ed8d432" />

# Else  
The else keyword catches anything which isn't caught by the preceding conditions.  
```python
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
```
<img width="214" height="28" alt="image" src="https://github.com/user-attachments/assets/30710377-4bf4-4982-9e5b-1f1dc211bb96" />

# And  
The and keyword is a logical operator, and is used to combine conditional statements:  
```python
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
```
<img width="269" height="32" alt="image" src="https://github.com/user-attachments/assets/4c0fdebb-4910-47b9-89b7-cce4d63e1426" />

# Or  
The or keyword is a logical operator, and is used to combine conditional statements:  
```python
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
```
<img width="417" height="33" alt="image" src="https://github.com/user-attachments/assets/09d4086d-0fab-410e-a4ae-3fba4f85ddd6" />

# Not  
The not keyword is a logical operator, and is used to reverse the result of the conditional statement:  
```python
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
```
<img width="253" height="44" alt="image" src="https://github.com/user-attachments/assets/2f915726-4d7c-499a-a34f-f09a0b7c2489" />

