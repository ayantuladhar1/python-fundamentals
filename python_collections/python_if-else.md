Python Conditions and If statements
Python supports the usual logical conditions from mathematics:
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

a = 33
b = 200
if b > a:
  print("b is greater than a")


Elif
The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


Else
The else keyword catches anything which isn't caught by the preceding conditions.

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


And
The and keyword is a logical operator, and is used to combine conditional statements:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


Or
The or keyword is a logical operator, and is used to combine conditional statements:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")



Not
The not keyword is a logical operator, and is used to reverse the result of the conditional statement:

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")


