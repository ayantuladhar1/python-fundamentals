# Add List Items

## Append Items
To add an item to the end of the list, use the append() method:

## Example:
Using append() method to append an item:
```python
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
```
<img width="349" height="41" alt="image" src="https://github.com/user-attachments/assets/dcd026e9-0e96-43d6-a14e-380677db7e21" />

## Insert Items
To insert a list item at a specified index, use the insert() method.
The insert() method inserts an item at the specified index:

## Example:
Insert an item as the second position:
```python
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
```
<img width="344" height="22" alt="image" src="https://github.com/user-attachments/assets/d2215802-5bb3-47b0-9ceb-563ceebc944c" />

## Extend List
To append elements from another list to the current list, use the extend() method.

## Example:
Ad the elements of tropical to thislist:
```python
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
```
<img width="550" height="39" alt="image" src="https://github.com/user-attachments/assets/73a83215-1b82-410b-9f37-7cb761ccf71f" />

## Add Any Iterable
The extend() method does not have to append lists, you can add any iterable object (tuples, sets,dictionaries, etc)

## Example:
Add elements of a tuple to a list:
```python
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
```
<img width="420" height="31" alt="image" src="https://github.com/user-attachments/assets/9af4295e-85c3-46ac-8b79-8c36dc645eba" />
