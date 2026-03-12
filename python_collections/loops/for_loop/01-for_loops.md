# Python For Loops
A for loop is used for iterating over a sequence (this is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of stataments, once for each item in a list, tuple, set, etc.

## Example:
Print each fruit in a fruit list:
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
```
<img width="80" height="83" alt="image" src="https://github.com/user-attachments/assets/c6737268-2387-4d4a-a093-a1e8b9d8af53" />

The for loop does not require an indexing variable to set beforehand.

## Looping Through a String
Even strings are iterable objects, they contian a sequence of characters:

## Example:
Loop through the letters in the word "banana":
```python
for x in "banana":
  print(x) 
```
<img width="33" height="168" alt="image" src="https://github.com/user-attachments/assets/081759d5-49a4-45f5-b5b4-60e022be2f41" />

## The Break Statement
With the break statement we can stop the loop before it has looped through all the items:

## Example:
Exit the loop when x is "banana":
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break
```
<img width="67" height="50" alt="image" src="https://github.com/user-attachments/assets/f3c8cb86-2bcb-4e56-8153-4e0a997c8b0d" />

## Example
Exit the loop when x is "banana", but this time the break comes before the print:
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
```
<img width="59" height="30" alt="image" src="https://github.com/user-attachments/assets/643ee4bb-110b-43fb-992b-df2e712d9ec8" />

## The Continue Statement
With the continue statement we can stop the current iteration of the loop, and continue with the next:

## Example:
Do not print banana:
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 
```
<img width="70" height="58" alt="image" src="https://github.com/user-attachments/assets/716b9bbd-27ee-4a03-ae01-8816179d862b" />

## The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default) and ends at a specified number.

## Example
Using the range() function:
```python
for x in range(6):
  print(x) 
```
<img width="31" height="175" alt="image" src="https://github.com/user-attachments/assets/793d2a6a-d34e-419e-b19a-22e7e6df2ef8" />

Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range (2,6), which means values from 2 to 6 (but not including 6).

## Example:
Using the start parameter:
```python
for x in range(2, 6):
  print(x) 
```
<img width="25" height="108" alt="image" src="https://github.com/user-attachments/assets/bf809e1b-2eed-4822-8f5b-41182f912e65" />

The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3).

## Example:
Increment the sequence with 3 (default is 1):
```python
for x in range(2, 30, 3):
  print(x) 
```
<img width="44" height="282" alt="image" src="https://github.com/user-attachments/assets/c7672532-0927-4825-93be-489f535bcb81" />

## Else in For Loop
The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

## Example:
Print all numbers from 0 to 5, and print a message when the loop has ended:
```python
for x in range(6):
  print(x)
else:
  print("Finally finished!")
```
<img width="180" height="195" alt="image" src="https://github.com/user-attachments/assets/90f1cb0f-3ad4-45ac-9d74-6108a04da5ff" />

Note: The else block will NOT be executed if the loop is stopped by a break statement.

## Example:
Break the loop when x is 3 and see what happends with the else block.
```python
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#If the loop breaks, the else block is not executed.
```
<img width="33" height="80" alt="image" src="https://github.com/user-attachments/assets/25e072be-ef60-46b9-88e1-e6f9c8b4cdaa" />

## Nested Loops
A nested loop is a loop inside a loop.
The "inner loop" will be execute one time for each iteration of the "outer loop".

## Example
```python
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
```
<img width="141" height="249" alt="image" src="https://github.com/user-attachments/assets/5a355bac-0b43-4431-8600-20ced5fdd01c" />

## The Pass Statement
For loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

## Example:
```python
for x in [0, 1, 2]:
  pass
# having an empty for loop like this, would raise an error without the pass statement
```
