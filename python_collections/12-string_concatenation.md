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
