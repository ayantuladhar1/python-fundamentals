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
