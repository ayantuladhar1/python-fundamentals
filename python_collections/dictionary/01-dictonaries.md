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
