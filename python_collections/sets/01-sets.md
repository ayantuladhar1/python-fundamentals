# Set
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is unordered, unchangeable, and unindexed.

Note: Set items are unchangeable, but you can remove items and add new items.

Sets are written with curly brackets.

## Example:
Create a Set:
```python
thisset = {"apple", "banana", "cherry"}
print(thisset)
```
<img width="255" height="34" alt="image" src="https://github.com/user-attachments/assets/aaf1ea9d-9af9-4e97-9d13-a28eebe70c9e" />

Note: Sets are unordered, so you cannot be sure in which order the items will appear.

## Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

## Unordered
Unordered means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

## Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.
Once a set is created, you cannot change its items, but you can remove items and add new items.

## Duplicates Not Allowed
Set cannot have two items with the same value.

## Example:
Duplicate values assigned will be ignored:
```python
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
```
<img width="260" height="34" alt="image" src="https://github.com/user-attachments/assets/6334799e-b280-4bac-b71a-34b61f03cf0d" />

Note: The value True and 1 are considered the same value in sets, and are treated as duplicates:

## Example:
True and 1 is considered the same value:
```python
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
```
<img width="343" height="36" alt="image" src="https://github.com/user-attachments/assets/1c58ffc6-2ee0-4804-a2d8-67653dd8e5e1" />

Note: The value False and 0 are considered the same value in sets and are treated as duplicates:

## Example:
False anbd 0 is considered the same value:
```python
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
```
<img width="378" height="29" alt="image" src="https://github.com/user-attachments/assets/5ae3af05-ca82-4588-8b20-d8d69a1a1544" />

## Get a Length of a Set
To determine how many items a set has, use the len() function.

## Example:
Get the number of items in a set:
```python
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
```
<img width="16" height="26" alt="image" src="https://github.com/user-attachments/assets/7e8d49e5-b58b-4312-b229-f11984fc02c4" />

## Set Items - Data Types
Set items can be of any data type:

## Example:
String, int and boolean data types:
```python
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)
```
<img width="267" height="87" alt="image" src="https://github.com/user-attachments/assets/564ca2dd-fd77-48c5-afe4-d50e48b1642a" />

A set can contain different data types:

## Example:
A set with strings, integers and boolean values:
```python
set1 = {"abc", 34, True, 40, "male"}
print(set1)
```
<img width="262" height="36" alt="image" src="https://github.com/user-attachments/assets/e6a74c21-6b66-46e3-93e0-83c32797bfdf" />

# type()
From Python's perspective, sets are defined as objects with the data type 'set':

## Example:
What is the data type of a set?
```python
myset = {"apple", "banana", "cherry"}
print(type(myset))
```
<img width="126" height="29" alt="image" src="https://github.com/user-attachments/assets/eb13a0f9-299d-41e0-bdcc-a558daa90d6f" />

## The set() Constructor
It is also possible to use the set() constructor to make a set.

## Example:
Using the set() constructor to make a set:
```python
thisset = set(("apple", "banana", "cherry"))
print(thisset)
# Note: the set list is unordered, so the result will display the items in a random order.
```
<img width="261" height="30" alt="image" src="https://github.com/user-attachments/assets/2c377c1f-3ba3-43c0-b0b5-c19791c4178b" />

# Python Collections (Arrays)
There are four collection data types in the Python programming language:
* List is a collection which is ordered and changeable. Allows duplicate members.
* Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
* Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
* Dictionary is a collection which is ordered** and changeable. No duplicate members.

Set Items are unchangeable but you can remove and add items.
