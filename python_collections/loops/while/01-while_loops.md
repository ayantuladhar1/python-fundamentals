# Python Loops
Python has two primitive loop commads:
* while loops
* for loops

## The While Loop
With the while loop we can execuute a set of statements as long as a condtion is true.

## Example:
Print i as long as i is less than 6:
```python
i = 1
while i < 6:
  print(i)
  i += 1
```
<img width="26" height="139" alt="image" src="https://github.com/user-attachments/assets/e89af566-be5e-4d5a-bcae-af59e2565f38" />

Note: Remember to increment i, or else the loop will continue foreever.

The while loop requires relavant variables to be ready, in this example we need to define an indexing variable i, which we set to 1.

## The break Statement
With the break statement we can stop the loop even if the while condition is true:

## Example:
Exit the loop when i is 3:
```python
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1
```
<img width="27" height="84" alt="image" src="https://github.com/user-attachments/assets/65f576d9-70ef-4304-ae14-309390d114f4" />
