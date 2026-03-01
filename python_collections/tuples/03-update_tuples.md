# Update Tuples
Tuples are unchangeable, meaning that you cannot change, add or remove items once the tuple is created.
But there are some workarounds.

## Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list and convert the list back into a tuple.

## Example:
Convert the tuple into a list to be able to change it:
```python
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
```
<img width="288" height="38" alt="image" src="https://github.com/user-attachments/assets/6a1d85be-71e0-468e-a05b-3d014796a7ff" />

## Add Items
Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

1. Convert into list: Just like the workaround for changing a tuple, you can convert it into a list, add your items and convert it back into a tuple.

## Example:
Convert the tuple into a list, add "orange", and convert it back into a tuple:
```python
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
```
<img width="404" height="34" alt="image" src="https://github.com/user-attachments/assets/c7da62b8-b1e7-41f6-88a4-4de282ea570a" />

2. Add tuple to a tuple, You are allowed to add tuples to tuples, so if you want to addd one item, or many,
create a new tuple with the items and add it to the existing tuple:

## Example:
Create a new tuple with the value "orange" and add that tuple:
```python
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
```
<img width="402" height="40" alt="image" src="https://github.com/user-attachments/assets/e8bfc58f-808c-4b72-b714-f80debb8e70a" />

Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.

## Remove Items
Note: You cannot remove items in a tuple.
Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

## Example:
Convert the tuple into a list, remove "apple", and convert it back into a tuple:
```python
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
```
<img width="209" height="38" alt="image" src="https://github.com/user-attachments/assets/52ba1c5d-da45-4a4f-a3ea-f538d0c5ab87" />

Or you can delete the tuple completely:

## Example:
The del keyword can delete the tuple completely:
```python
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
```

