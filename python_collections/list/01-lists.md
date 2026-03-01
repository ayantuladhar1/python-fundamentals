# List
Lists are used to store multiple items in a single variable.
Lists are one of a 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set and Dictionary, all with different qualities and usage.
List are created using square brackets.

## Example:
```python
thislist = ["apple","banana", "cherry"]
prrint(thislist)
```
<img width="263" height="31" alt="image" src="https://github.com/user-attachments/assets/da633669-dcc1-48e9-8553-0eaa74c5d39f" />

## List Items
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.

## Ordered 
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the first.

## Note: There are some list methods that will change the order, but in general, the order of the items will not change.

## Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

## Allow Duplicates
Since lists are indexed, lists can have items with the same value:

## Example:
List allows duplicate values:
```python
thislist = ["apple", "banana', "cherrry", "apple", "cherry"]
print(thislist)
```
<img width="433" height="49" alt="image" src="https://github.com/user-attachments/assets/ed36417e-5079-4edb-ad1a-4adc7c6cd792" />

## List Length
To determine how many items a list has, use the len() function.

## Example:
List allows duplicate values:
```python
thislist = ["apple", "banana', "cherrry"]
print(len(thislist))
```

## List Items - Data Types
List items can be of any data type:

## Example:
```pyhton
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, True]
print(list1)
print(list2)
print(list3)
```
<img width="264" height="89" alt="image" src="https://github.com/user-attachments/assets/4f8153e6-8255-422f-84e1-26e112deb5a5" />

A list can contain different types:

## Example:
A list with strings, integeres and boolean values:
```python
list1 = ["abc", 34, True, 40, "male"]
print(list1)
```
<img width="266" height="34" alt="image" src="https://github.com/user-attachments/assets/b3842ded-d590-47dd-ae18-4bc35232b0e2" />

## type()
From Python's perspective, lists are defined as objects with the data type 'list':
```python
<class 'list'>
```

## Example:
What is the data type of a list
```python
mylits = ["apple", "banana", "cherry"]
print(type(mylist))
```
<img width="137" height="33" alt="image" src="https://github.com/user-attachments/assets/d6689374-b419-4b28-847f-8d9115d4939b" />

## The list() Constructor
It is also possible to use list() constructor when creating a new list.

## Example:
Uisng the list() constructor when creating a new list.
```python
thislist = list(("apple", "banana", "cherry")) # note the double round brackets.
print(thislist)
```
<img width="264" height="33" alt="image" src="https://github.com/user-attachments/assets/7bd848c5-a871-453b-af2e-0ab295aa3d00" />

# Python Collection (Arrays)
There are four collection data types in the Python programming language:
* List is a collection which is ordered and changeable. Allows duplicate members.
* Tuple is a collection which is ordered and unchangeable. Allow duplicate members.
* Set is a collection which is unordered, unchangeable and unindexed. No duplicate members.
* Dictionary is a collection which is ordered and changeable. No duplicate members.
