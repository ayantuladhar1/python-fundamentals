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
## Evaluate Values and Variables
The bool() function allows you to evaluate any value, and give you True or False in return.

<img width="960" height="603" alt="image" src="https://github.com/user-attachments/assets/c952760a-30da-41c5-a413-bfd0c63fc57e" />
<img width="852" height="123" alt="image" src="https://github.com/user-attachments/assets/8491346b-756b-467c-a950-e2d42d1ea150" />
<img width="941" height="445" alt="image" src="https://github.com/user-attachments/assets/b3de6c26-b228-466c-a70d-9c8afaed61d9" />
<img width="856" height="166" alt="image" src="https://github.com/user-attachments/assets/55c522c5-3bba-47db-9f5d-84fd53cb0c12" />

