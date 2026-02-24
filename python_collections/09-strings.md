# Strings
Strings in python are surrounded by either single quotation marks or double quotation marks.
You can display a string literal with the print() function.

## Multiline Strings
You can assign a multiline string to a variable by using three quotes:
```python
#Multiline Strings
a = """Lorem ipsum dolor sit amet, 
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```
<img width="368" height="98" alt="image" src="https://github.com/user-attachments/assets/0508fb53-5bcf-4e52-af66-7bc7a9463b84" />

## Or three single quotes
```python
a = '''Lorem ipsum dolor sit amet,  
consectetur adipiscing elit,  
sed do eiusmod tempor incididunt  
ut labore et dolore magna aliqua.'''  
print(a)
```
<img width="360" height="87" alt="image" src="https://github.com/user-attachments/assets/f49ee111-99d1-429b-91bb-46621478e185" />

## Assign String to a Variable

Assigning a string to a variable is done with the variable name followed by an equal sign and the string.

<img width="649" height="91" alt="image" src="https://github.com/user-attachments/assets/e1f1a4bf-359f-4ad9-aac1-a5d11cb83b55" />

## Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of Unicode characters.
However, Python does not have a character data type, a single character is simply a string with length of 1.
Square brackets [] can be used to access elements of the string.

<img width="942" height="386" alt="image" src="https://github.com/user-attachments/assets/66e8f3e4-3ce8-4a42-8be1-572112026860" />
<img width="38" height="45" alt="image" src="https://github.com/user-attachments/assets/0269ca9c-c700-427f-b432-14dcc1aeb4f7" />

## Looping through String
Since strings are arrays, we can loop through the characters in a string with a for loop.

<img width="948" height="339" alt="image" src="https://github.com/user-attachments/assets/211be37a-5ad5-44df-96f8-b5e7d6ae5645" />
<img width="795" height="244" alt="image" src="https://github.com/user-attachments/assets/b650fe44-6cc4-445e-83ec-e7739523f0d1" />

## String Length
To get the length of a string, use the len() function.

<img width="950" height="345" alt="image" src="https://github.com/user-attachments/assets/ab5995fa-3f99-472b-8b41-c8cb2c297941" />
<img width="831" height="115" alt="image" src="https://github.com/user-attachments/assets/ed05fb91-f9dc-4eae-8ca8-72e14d0d4377" />

## Check String

To check if a certain phrase or character is present in a string, we can use the keyword in.

<img width="949" height="345" alt="image" src="https://github.com/user-attachments/assets/bc8df0ad-fb11-43be-8ca5-4916f71e0a5f" />
<img width="856" height="91" alt="image" src="https://github.com/user-attachments/assets/4464d96f-333c-4d58-b07c-745f460381af" />

## Use it in an if statement

<img width="949" height="371" alt="image" src="https://github.com/user-attachments/assets/28e06ecc-2526-41d4-9f29-cf250e587226" />
<img width="1105" height="110" alt="image" src="https://github.com/user-attachments/assets/053ce4ea-a928-404b-a3ad-aeb2fbe3af31" />

## Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in

<img width="938" height="340" alt="image" src="https://github.com/user-attachments/assets/0248c927-1762-445f-ab21-6b8e7f0ab7d8" />
<img width="855" height="86" alt="image" src="https://github.com/user-attachments/assets/3f5ef005-a71c-4a11-96ee-b88130a1b2e1" />

## Use it in an if statement

<img width="941" height="369" alt="image" src="https://github.com/user-attachments/assets/eece0e57-9a5d-44d4-bbe8-e46c332c6464" />
<img width="1204" height="114" alt="image" src="https://github.com/user-attachments/assets/db651032-c65a-4a23-a45c-dab2818ad972" />

## The upper() method returns the string in upper case:  
```python
a = "Hello, World!"  
print(a.upper())  
```
<img width="154" height="30" alt="image" src="https://github.com/user-attachments/assets/de1335db-2eee-4b4b-ad37-eef175801e79" />

## The lower() method returns the string in lower case:  
```python
a = "Hello, World!"  
print(a.lower())  
```
<img width="147" height="25" alt="image" src="https://github.com/user-attachments/assets/97a5a6d9-4885-47f3-ad59-0cf98a60d152" />

## The strip() method removes any whitespace from the beginning or the end:  
```python
a = " Hello, World! "  
print(a.strip()) # returns "Hello, World!"  
```
<img width="142" height="24" alt="image" src="https://github.com/user-attachments/assets/595360e8-267d-4eb1-9997-1bd3d7e5bfb5" />

## The replace() method replaces a string with another string:  
```python
a = "Hello, World!"  
print(a.replace("H", "J"))  
```
<img width="148" height="22" alt="image" src="https://github.com/user-attachments/assets/e9dc636d-7f36-4b51-b74f-e3d3e2aaaa6a" />

## The split() method splits the string into substrings if it finds instances of the separator:  
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

## To add a space between them, add " ":  
```python
a = "Hello"  
b = "World"  
c = a + " " + b  
print(c)  
```
<img width="132" height="36" alt="image" src="https://github.com/user-attachments/assets/25f298f6-beb9-4f46-ab4d-c51ebf882723" />

## We cannot combine strings and numbers like this:  
```python
age = 36  
txt = "My name is John, I am " + age  
print(txt)  
```

## But we can combine strings and numbers by using the format() method!  
The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:  
Use the format() method to insert numbers into strings:  
```python
age = 36  
txt = "My name is John, and I am {}"  
print(txt.format(age))  
```
<img width="305" height="32" alt="image" src="https://github.com/user-attachments/assets/0c15bc1c-ff5a-43a7-89ec-a06351a4caf3" />

## The format() method takes unlimited number of arguments, and are placed into the respective placeholders:  
```python
quantity = 3  
itemno = 567  
price = 49.95  
myorder = "I want {} pieces of item {} for {} dollars."  
print(myorder.format(quantity, itemno, price))  
```
<img width="500" height="38" alt="image" src="https://github.com/user-attachments/assets/a6cffb74-117c-439a-be32-0a17ec777854" />

## You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:  
```python
quantity = 3  
itemno = 567    
price = 49.95  
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."  
print(myorder.format(quantity, itemno, price))  
```
<img width="571" height="34" alt="image" src="https://github.com/user-attachments/assets/034c0059-f44c-4a19-904b-a42f81e7e5d6" />
