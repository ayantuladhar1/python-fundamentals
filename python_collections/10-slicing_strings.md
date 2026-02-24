# Slicing Strings  
You can return a range of characters by using the slice syntax.  
Specify the start index and the end index, separated by a colon, to return a part of the string.  
Get the characters from position 2 to position 5 (not included):  

```python
b = "Hello, World!"  
print(b[2:5])
```
<img width="34" height="24" alt="image" src="https://github.com/user-attachments/assets/24cb655c-2662-4e58-9a78-f722744b7046" />

## Get the characters from the start to position 5 (not included):  
```python
b = "Hello, World!"  
print(b[:5])  
```
<img width="60" height="26" alt="image" src="https://github.com/user-attachments/assets/58a7ee04-b830-4367-aea7-174ac659a9fe" />

## Get the characters from position 2, and all the way to the end:  
```python
b = "Hello, World!"  
print(b[2:])  
```
<img width="124" height="33" alt="image" src="https://github.com/user-attachments/assets/547095aa-802d-4990-b7c1-8a2b35e0e534" />

## Negative Indexing  
Use negative indexes to start the slice from the end of the string:  
Get the characters:  
From: "o" in "World!" (position -5)  
To, but not included: "d" in "World!" (position -2) not included:  
```python
b = "Hello, World!"  
print(b[-5:-2])  
```
<img width="42" height="36" alt="image" src="https://github.com/user-attachments/assets/63de9e81-206d-45ea-b7cf-4f22c29191ff" />
