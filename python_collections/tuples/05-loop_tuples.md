# Loop Through a Tuple
You can loop through the tuple by using a for loop.

## Example:
Iterate through the item and print the values:
```python
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
```
<img width="72" height="77" alt="image" src="https://github.com/user-attachments/assets/d656060b-5f3d-4569-853d-1503579eac40" />

## Loop Through the Index Numbers
You can also loop through the tuple items by referring to their index number.
Use the range() and len() functions to create a suitable iterable.

## Example:
Print all items by referring to their index number:
```python
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
```
<img width="63" height="69" alt="image" src="https://github.com/user-attachments/assets/fce71a3c-4008-46cc-830c-119406519226" />

## USing a While Loop
You can loop through the tuple items by using a while loop.
Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.
Remember to increase the index by 1 after each iteration.

## Example:
Print all items, using a while loop to go through all the index numbers:
```python
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
```
<img width="68" height="71" alt="image" src="https://github.com/user-attachments/assets/c2716356-1a0f-49fb-a5b9-0c5cb91b5149" />
