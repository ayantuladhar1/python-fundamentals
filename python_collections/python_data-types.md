# Built-in Data Types
|Text Type|str|
|---------|---|
|Numeric Types| int, float|
|Sequence Types| list, tuple|
|Mapping Type| dict|
|Set Types| set|
|Boolean Type| bool|


|Example | Data Type|
|----------|------------|
|x = "Hello World" | str |
|x = 20 | int |
|x = 20.5 |	float |
|x = 1j |complex |
|x = ["apple", "banana", "cherry"] | list |
|x = ("apple", "banana", "cherry") | tuple |
|x = range(6) | range |
|x = {"name" : "John", "age" : 36} | dict |
|x = {"apple", "banana", "cherry"} | set |
|x = True |	bool |
  
  
```python
#Multiline Strings
a = """Lorem ipsum dolor sit amet, 
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```
<img width="368" height="98" alt="image" src="https://github.com/user-attachments/assets/0508fb53-5bcf-4e52-af66-7bc7a9463b84" />

```python
a = '''Lorem ipsum dolor sit amet,  
consectetur adipiscing elit,  
sed do eiusmod tempor incididunt  
ut labore et dolore magna aliqua.'''  
print(a)
```
<img width="360" height="87" alt="image" src="https://github.com/user-attachments/assets/f49ee111-99d1-429b-91bb-46621478e185" />

# Python - Slicing Strings  
You can return a range of characters by using the slice syntax.  
Specify the start index and the end index, separated by a colon, to return a part of the string.  
Get the characters from position 2 to position 5 (not included):  

```python
b = "Hello, World!"  
print(b[2:5])
```
<img width="34" height="24" alt="image" src="https://github.com/user-attachments/assets/24cb655c-2662-4e58-9a78-f722744b7046" />

# Get the characters from the start to position 5 (not included):  
```python
b = "Hello, World!"  
print(b[:5])  
```
<img width="60" height="26" alt="image" src="https://github.com/user-attachments/assets/58a7ee04-b830-4367-aea7-174ac659a9fe" />

# Get the characters from position 2, and all the way to the end:  
```python
b = "Hello, World!"  
print(b[2:])  
```
<img width="124" height="33" alt="image" src="https://github.com/user-attachments/assets/547095aa-802d-4990-b7c1-8a2b35e0e534" />

# Negative Indexing  
Use negative indexes to start the slice from the end of the string:  
Get the characters:  
From: "o" in "World!" (position -5)  
To, but not included: "d" in "World!" (position -2) not included:  
```python
b = "Hello, World!"  
print(b[-5:-2])  
```
<img width="42" height="36" alt="image" src="https://github.com/user-attachments/assets/63de9e81-206d-45ea-b7cf-4f22c29191ff" />

# The upper() method returns the string in upper case:  
```python
a = "Hello, World!"  
print(a.upper())  
```
<img width="154" height="30" alt="image" src="https://github.com/user-attachments/assets/de1335db-2eee-4b4b-ad37-eef175801e79" />

# The lower() method returns the string in lower case:  
```python
a = "Hello, World!"  
print(a.lower())  
```
<img width="147" height="25" alt="image" src="https://github.com/user-attachments/assets/97a5a6d9-4885-47f3-ad59-0cf98a60d152" />

# The strip() method removes any whitespace from the beginning or the end:  
```python
a = " Hello, World! "  
print(a.strip()) # returns "Hello, World!"  
```
<img width="142" height="24" alt="image" src="https://github.com/user-attachments/assets/595360e8-267d-4eb1-9997-1bd3d7e5bfb5" />

# The replace() method replaces a string with another string:  
```python
a = "Hello, World!"  
print(a.replace("H", "J"))  
```
<img width="148" height="22" alt="image" src="https://github.com/user-attachments/assets/e9dc636d-7f36-4b51-b74f-e3d3e2aaaa6a" />

# The split() method splits the string into substrings if it finds instances of the separator:  
```python
a = "Hello, World!"  
print(a.split(",")) # returns ['Hello', ' World!']  
```
<img width="219" height="31" alt="image" src="https://github.com/user-attachments/assets/a4a2f9bd-8d5c-405c-b3b8-e75efc0622d9" />

# String Concatenation  
Merge variable a with variable b into variable c:  
```python
a = "Hello"  
b = "World"  
c = a + b  
```

# To add a space between them, add " ":  
```python
a = "Hello"  
b = "World"  
c = a + " " + b  
print(c)  
```
<img width="132" height="36" alt="image" src="https://github.com/user-attachments/assets/25f298f6-beb9-4f46-ab4d-c51ebf882723" />

# we cannot combine strings and numbers like this:  
```python
age = 36  
txt = "My name is John, I am " + age  
print(txt)  
```

# But we can combine strings and numbers by using the format() method!  
The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:  
Use the format() method to insert numbers into strings:  
```python
age = 36  
txt = "My name is John, and I am {}"  
print(txt.format(age))  
```
<img width="305" height="32" alt="image" src="https://github.com/user-attachments/assets/0c15bc1c-ff5a-43a7-89ec-a06351a4caf3" />

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:  
```python
quantity = 3  
itemno = 567  
price = 49.95  
myorder = "I want {} pieces of item {} for {} dollars."  
print(myorder.format(quantity, itemno, price))  
```
<img width="500" height="38" alt="image" src="https://github.com/user-attachments/assets/a6cffb74-117c-439a-be32-0a17ec777854" />

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:  
```python
quantity = 3  
itemno = 567    
price = 49.95  
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."  
print(myorder.format(quantity, itemno, price))  
```
<img width="571" height="34" alt="image" src="https://github.com/user-attachments/assets/034c0059-f44c-4a19-904b-a42f81e7e5d6" />

# Boolean Values  
In programming you often need to know if an expression is True or False.  
You can evaluate any expression in Python, and get one of two answers, True or False.  
When you compare two values, the expression is evaluated and Python returns the Boolean answer:  
```python
print(10 > 9)  
print(10 == 9)  
print(10 < 9)  
```
<img width="64" height="71" alt="image" src="https://github.com/user-attachments/assets/86bae03f-ab30-479b-b8f4-8a78bda3665c" />

# Print a message based on whether the condition is True or False:  
```python
a = 200  
b = 33  
if b > a:  
  print("b is greater than a")   
else:  
  print("b is not greater than a")  
```
<img width="256" height="28" alt="image" src="https://github.com/user-attachments/assets/b14479fe-af62-4e93-9ac7-056609384cc3" />

# Most Values are True  
Almost any value is evaluated to True if it has some sort of content.  
Any string is True, except empty strings.  
Any number is True, except 0.  
Any list, tuple, set, and dictionary are True, except empty ones.  
The following will return True:  
```python
bool("abc")  
bool(123)  
bool(["apple", "cherry", "banana"])  
```

# Some Values are False  
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.  
The following will return False:  
```python
bool(False)  
bool(None)  
bool(0)  
bool("")  
bool(())  
bool([])  
```

# Numbers  
```python
x = 1    # int  
y = 2.8  # float  
```

# Int  
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.  
```python
x = 1  
y = 35656222554887711  
z = -3255522  
print(type(x))  
print(type(y))  
print(type(z))  
```
<img width="147" height="69" alt="image" src="https://github.com/user-attachments/assets/6cb17d35-0ee4-4eaa-b34a-41ed9bb8b5ee" />

# Float  
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.  
```python
x = 1.10  
y = 1.0  
z = -35.59  
print(type(x))  
print(type(y))  
print(type(z))  
```
<img width="175" height="72" alt="image" src="https://github.com/user-attachments/assets/10dd7329-7686-44f7-b2ff-b8aa599a77d7" />

# Type Conversion  
You can convert from one type to another with the int(), float()  
Convert from one type to another:  
```python
x = 1    # int  
y = 2.8  # float  
```

# Convert from int to float:  
```python
a = float(x)  
```

# Convert from float to int:  
```python
b = int(y)  
  
print(a)  
print(b)  
 
print(type(a))  
print(type(b))  
```
<img width="178" height="93" alt="image" src="https://github.com/user-attachments/assets/da983aa6-5ac4-481f-becb-8fff3304daf3" />

# Random Number  
Import the random module, and display a random number between 1 and 9:  
import random
```python
print(random.randrange(1, 10))  
```
<img width="29" height="38" alt="image" src="https://github.com/user-attachments/assets/8a594b6c-ea9a-4f94-a5b9-92783f855cea" />
