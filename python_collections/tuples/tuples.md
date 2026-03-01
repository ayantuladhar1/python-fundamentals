# Tuple
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 aare List, Set and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.

## Example:
Create a Tuple:
```python
thistuple = ("apple", "banana", "cherry")
print(thistuple)
```
<img width="259" height="32" alt="image" src="https://github.com/user-attachments/assets/58ffbd54-cf1c-458d-a647-ca5accd28b92" />

## Tuple Items
Tuple items are ordered, unchangeable and allo duplicate values.
Tuple items are indexed, the first item has index [0], the second item has index [1], etc.

## Ordered
When we say that tuples are ordered, it means that the items have defined order, and that order will not change.

## Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

## Allow Duplicates
Since tuples are indexed, that can have items with same value:

## Example:
Tuple allow duplicate values:
```python
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
```
<img width="425" height="30" alt="image" src="https://github.com/user-attachments/assets/e1844264-e574-488b-8e76-d708fc534b80" />

## Tuple Length
To determine how many items atuple has, use the len() function:

## Example:
```python
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
```
<img width="22" height="29" alt="image" src="https://github.com/user-attachments/assets/e32d494f-f6d9-433e-ac02-335811bf4a3b" />

## Create Tuple With One Item
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

## Example:
One item tuple, remember the comma:
```python
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
```
<img width="144" height="57" alt="image" src="https://github.com/user-attachments/assets/470127fa-25cb-42ed-bc54-2b6baae228d0" />

## Tuple Items - Data Types
Tuple items can be of any data type:

## Example:
String, int and booleand data types:
```python
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)
```
<img width="267" height="87" alt="image" src="https://github.com/user-attachments/assets/f6444c9d-ce17-40af-8bc5-fdcf7d93d3e4" />

A tuple can contain different data types:

## Example:
```python
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
```
<img width="261" height="30" alt="image" src="https://github.com/user-attachments/assets/2923f873-30a3-45c7-ae99-900624692368" />

## type()
From Python's perspective, tuples are defined as objects with the data type 'tuple':

## Example:
What is the dat type of a tuple?
```python
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
```
<img width="143" height="31" alt="image" src="https://github.com/user-attachments/assets/8b650592-1975-43b5-9796-65a79ec40b26" />

## The tuple() Constructor
It is alos possible to use the tuple() constructor to make a tuple.

## Example:
Using the tuple() method to make a tuple:
```python
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
```
<img width="258" height="30" alt="image" src="https://github.com/user-attachments/assets/a493e4be-cde0-483f-8fac-4ab1d3fd519d" />

# Python Collections (Arrays)
There are four collection data types in the Python programming language:
* List is a collection which is ordered and changeable. Allows duplicate members.
* Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
* Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
* Dictionary is a collection which is ordered** and changeable. No duplicate members.
