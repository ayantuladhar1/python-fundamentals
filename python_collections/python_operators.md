# In the example below, we use the + operator to add together two values:  
```python
print(10 + 5)  
```
|Python | Arithmetic | Operators |
|-------|------------|-----------|
|+ | Addition |	x + y|
|- | Subtraction | x - y|
|* | Multiplication	|x * y|
|/ | Division | x / y|
|% | Modulus | x % y|
|**	| Exponentiation | x ** y|
|//	| Floor division | x // y|  
  
  
# Python Assignment Operators  
Assignment operators are used to assign values to variables:  
  
|Operator | Example |	Same As|
|---------|---------|--------|
|=		|	x = 5	|	x = 5|
|+=			|x += 3	|	x = x + 3|
|-=		|	x -= 3	|	x = x - 3|
|*=		|	x *= 3	|	x = x * 3|
|/=		|	x /= 3	|	x = x / 3|
|%=		|	x %= 3	|	x = x % 3|
|//=	|		x //= 3	|	x = x // 3|
|**=	|		x **= 3	|	x = x ** 3|
|&=		|	x &= 3	|	x = x & 3|
|type=		|	x type= 3	|	x = x type 3|
|^=		|	x ^= 3	|	x = x ^ 3|
|>>=	|		x >>= 3	|	x = x >> 3|
|<<=	|		x <<= 3	|	x = x << 3|  
  
  
# Python Comparison Operators  
Comparison operators are used to compare two values:  
  
|Operator | Name 			|			Example|
|---------|-----------|------------|
|==		|	Equal				|		x == y|
|!=			|Not equal		|			x != y|
|>			|Greater than		|		x > y|
|<		|	Less than			|		x < y|
|>=		|	Greater than or equal to|	x >= y|
|<=		|	Less than or equal to		|x <= y|
  
  
# Some Examples  
```python
x = 5  
y = 3   
print(x == y)  
```
  
# Python Logical Operators  
Logical operators are used to combine conditional statements:  
  
|Operator |	Description 		|										Example|
|---------|-----------------|--------------------------|
|and|       	Returns True if both statements are true			|		x < 5 and  x < 10|
|or		|	Returns True if one of the statements is true			|	x < 5 or x < 4|
|not		|	Reverse the result, returns False if the result is true	|	not(x < 5 and x < 10)|
  
  
# Some Examples  
```python
x = 5  
print(x > 3 and x < 10)  
```
  
# Python Identity Operators  
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:  
  
|Operator |	Description	|	Example |
|---------|-------------|---------|
|is 	|		Returns True if both variables are the same object	|	x is y|
|is not	|	Returns True if both variables are not the same object |	x is not y|
  
  
# Some Examples  
```python
x = ["apple", "banana"]  
y = ["apple", "banana"]  
z = x  
print(x is z)  
```

# Returns True because z is the same object as x  
```python
print(x is y)  
```
# Returns False because x is not the same object as y, even if they have the same content  
```python
print(x == y)  
  
x = ["apple", "banana"]  
y = ["apple", "banana"]  
z = x  
  
print(x is not z)  
  ```
* Returns False because z is the same object as x  
```python
print(x is not y)  
 ``` 
* Returns True because x is not the same object as y, even if they have the same content  
```python
print(x != y)  
  ```
  
# Python Membership Operators
Membership operators are used to test if a sequence is presented in an object:

|Operator|Description|Example|
|--------|-----------|-------|
|in|Returns True if a sequence with the specified value is present in the object|x in y|
|not in	|Returns True if a sequence with the specified value is not present in the object|x not in y|
