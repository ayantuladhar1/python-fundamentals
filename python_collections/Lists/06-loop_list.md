# Loop List
You can loop through the list items by using a for loop:

## Example:
Print all items in the list, one by one:
```python
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
```
<img width="68" height="77" alt="image" src="https://github.com/user-attachments/assets/cc96b5e1-8d41-4182-945e-e56a04a44201" />

## Loop Through the Index Numbers
You can also loop through the list items by referring to their index number.
Use the range() and len() functions to create a suitable iterable.

## Example:
Print all items by referring to thei index number.
```python
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
```
<img width="69" height="81" alt="image" src="https://github.com/user-attachments/assets/be5e48f4-d25f-4360-a269-d20c2930a9b1" />

The iterable created in the example aboce is [0, 1, 2].

## Using While Loop
You can loop through the list items by using a while loop
Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
Remember to increase the index by 1 after each iteration.

## Example:
Print all items using a while loop to go through all the index numbers
```python
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len (thislist):
  print(thislist[i])
  i = i + 1
```
<img width="65" height="85" alt="image" src="https://github.com/user-attachments/assets/d40c84eb-2b86-4a54-9408-e1be0f1391fe" />

## Looping Using List Comprehencion
List Comprehension offers shortest syntax for looping through lists:

## Example:
A short hand for loop that will print all items in a list:
```python
thislist = ["apple", "banana", "cherry']
[print(x) for x in thislist]
```
<img width="69" height="84" alt="image" src="https://github.com/user-attachments/assets/73f47087-5ab4-4a38-a2fd-224111e3c497" />
