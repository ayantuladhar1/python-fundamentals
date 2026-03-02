# Dictionary
Dictionaries are used to store values in key:value pairs.
A dictionary is a collection which is ordered, changeable and do not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values:

## Example:
Create and print a dictionary:
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
```
<img width="526" height="42" alt="image" src="https://github.com/user-attachments/assets/b656bd34-e94d-4c1f-b7db-9cb9fea4085d" />

## Dictionary Items
Dictionary items are ordered, changeable and do not allow duplicates.
Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

## Example:
Print the "brand" value of the dictionary:
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
```
<img width="51" height="27" alt="image" src="https://github.com/user-attachments/assets/ca84ea30-f23f-461c-b645-9430100b1b63" />

## Ordered or Unordered?
When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

## Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

## Duplicates Not Allowed
Dictionaries cannot have two items with the same key:

## Example:
Duplicate values will overwrite existing values:
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
```
<img width="523" height="44" alt="image" src="https://github.com/user-attachments/assets/f058004b-2b0a-4007-9608-58c7fb14880a" />

## Dictionary Length
To determine how many items a dictionary has, use the len() function.

## Example:
Print the number of items in the dictionary:
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))
```
<img width="22" height="28" alt="image" src="https://github.com/user-attachments/assets/9509c543-88d5-486b-909e-76d59c45de87" />

## Dictionary Items - Data Types
The values in dictionary items can be of any data type:

## Example:
String, int, boolean and list data types:
```python
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
```
<img width="884" height="38" alt="image" src="https://github.com/user-attachments/assets/c8fb35f9-58de-4022-8166-172bd1ffdd3e" />

## type()
From Python's perspective, dictionaries are defined as objects with the data type 'dict':

## Example:
Print the data type of a dictionary:
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
```

## The dict() Constructor
It is also possible to use the dict() constructor to make a dictionary.

## Example
Using the dict(0 method to make a dictionary:
```python
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) 
```
<img width="491" height="39" alt="image" src="https://github.com/user-attachments/assets/4998a099-6d4c-4ebc-8287-d49bcb25e25a" />

# Python Collections (Arrays)
There are four collection data types in the Python programming language:
* List is a collection which is ordered and changeable. Allows duplicate members.
* Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
* Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
* Dictionary is a collection which is ordered** and changeable. No duplicate members.
