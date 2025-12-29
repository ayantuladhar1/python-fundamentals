**Built-in Data Types**
* Text Type: str
* Numeric Types: int, float
* Sequence Types: list, tuple
* Mapping Type: dict
* Set Types: set
* Boolean Type: bool


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

```python
a = '''Lorem ipsum dolor sit amet,  
consectetur adipiscing elit,  
sed do eiusmod tempor incididunt  
ut labore et dolore magna aliqua.'''  

print(a)
```

#Python - Slicing Strings  
You can return a range of characters by using the slice syntax.  
Specify the start index and the end index, separated by a colon, to return a part of the string.  
Get the characters from position 2 to position 5 (not included):  

```python
b = "Hello, World!"  
print(b[2:5])
```


#Get the characters from the start to position 5 (not included):  
```python
b = "Hello, World!"  
print(b[:5])  
```

#Get the characters from position 2, and all the way to the end:  
```python
b = "Hello, World!"  
print(b[2:])  
```

#Negative Indexing  
Use negative indexes to start the slice from the end of the string:  
Get the characters:  
From: "o" in "World!" (position -5)  
To, but not included: "d" in "World!" (position -2) not included:  
```python
b = "Hello, World!"  
print(b[-5:-2])  
```

#The upper() method returns the string in upper case:  
```python
a = "Hello, World!"  
print(a.upper())  
```

#The lower() method returns the string in lower case:  
```python
a = "Hello, World!"  
print(a.lower())  
```

#The strip() method removes any whitespace from the beginning or the end:  
```python
a = " Hello, World! "  
print(a.strip()) # returns "Hello, World!"  
```

#The replace() method replaces a string with another string:  
```python
a = "Hello, World!"  
print(a.replace("H", "J"))  
```

#The split() method splits the string into substrings if it finds instances of the separator:  
```python
a = "Hello, World!"  
print(a.split(",")) # returns ['Hello', ' World!']  
```

#String Concatenation  
Merge variable a with variable b into variable c:  
```python
a = "Hello"  
b = "World"  
c = a + b  
```

#To add a space between them, add " ":  
```python
a = "Hello"  
b = "World"  
c = a + " " + b  
print(c)  
```

#we cannot combine strings and numbers like this:  
```python
age = 36  
txt = "My name is John, I am " + age  
print(txt)  
```

#But we can combine strings and numbers by using the format() method!  
The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:  
Use the format() method to insert numbers into strings:  
```python
age = 36  
txt = "My name is John, and I am {}"  
print(txt.format(age))  
```

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:  
```python
quantity = 3  
itemno = 567  
price = 49.95  
myorder = "I want {} pieces of item {} for {} dollars."  
print(myorder.format(quantity, itemno, price))  
```

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:  
```python
quantity = 3  
itemno = 567    
price = 49.95  
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."  
print(myorder.format(quantity, itemno, price))  
```

#Boolean Values  
In programming you often need to know if an expression is True or False.  
You can evaluate any expression in Python, and get one of two answers, True or False.  
When you compare two values, the expression is evaluated and Python returns the Boolean answer:  
```python
print(10 > 9)  
print(10 == 9)  
print(10 < 9)  
```

#Print a message based on whether the condition is True or False:  
```python
a = 200  
b = 33  
if b > a:  
  print("b is greater than a")   
else:  
  print("b is not greater than a")  
```

#Most Values are True  
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

#Some Values are False  
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

#Numbers  
```python
x = 1    # int  
y = 2.8  # float  
```

#Int  
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.  
```python
x = 1  
y = 35656222554887711  
z = -3255522  
print(type(x))  
print(type(y))  
print(type(z))  
```

#Float  
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.  
```python
x = 1.10  
y = 1.0  
z = -35.59  
print(type(x))  
print(type(y))  
print(type(z))  
```

#Type Conversion  
You can convert from one type to another with the int(), float()  
Convert from one type to another:  
```python
x = 1    # int  
y = 2.8  # float  
```

#convert from int to float:  
```python
a = float(x)  
```

#convert from float to int:  
```python
b = int(y)  
  
print(a)  
print(b)  
 
print(type(a))  
print(type(b))  
```

#Random Number  
Import the random module, and display a random number between 1 and 9:  
import random
```python
print(random.randrange(1, 10))  
```
