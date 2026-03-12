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

## The Continue Statement
With the continue statement we can stop the current iteration, and continue with the next.

## Example:
Continue to the next iteration if i is 3:
```python
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
# Note that number 3 is missing in the result
```
<img width="29" height="137" alt="image" src="https://github.com/user-attachments/assets/39449941-53cc-41c0-8a86-0bd7d3204654" />

## The else Statement
With the else statement we can run a block of code when the condition no longer is true.

## Example:
Print a message once the condition is false:
```python
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
```
<img width="281" height="169" alt="image" src="https://github.com/user-attachments/assets/e8e8f5ac-eccc-42b8-a4b2-dad5300e1bfa" />

Note: The else block will NOT be executed if the loop is stopped by a break statement.
