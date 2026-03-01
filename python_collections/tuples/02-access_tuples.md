# Access Tuple Items
You can access tuple items by referring to the index number, inside square brackets:

## Example:
Print the second item in the tuple:
```python
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
```
<img width="66" height="28" alt="image" src="https://github.com/user-attachments/assets/f68ed352-00c4-426a-8b72-dbdd4c762a2e" />

Note: The first item has index 0.

## Negative Indexing
Negative indexing means start from the end.
-1 refers to the last item, -2 referes to the second last item, etc.

## Example:
Print the last item of the tuple:
```python
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
```
<img width="68" height="31" alt="image" src="https://github.com/user-attachments/assets/e78b1397-64da-4164-b9e4-1a45a834c2cd" />

## Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new tuple with the specified items.

## Example:
Return the third, fourth, and fifth item:
```python
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
```
<img width="250" height="31" alt="image" src="https://github.com/user-attachments/assets/c2f8c5eb-d729-40e3-acd5-13b1a99152be" />

This will return the items from position 2 to 5.
Remember that the first item is position 0 and note that the item in position 5 is NOT included.

By leaving out the start value, the range will start at the first item:

## Example:
This examplee returns the items from the beginning to, but NOT included 'kiwi':
```python
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
```
<img width="350" height="33" alt="image" src="https://github.com/user-attachments/assets/582bfe2b-82e9-4f12-9549-d1d6223d2410" />

By leaving out the end value, the range will go on to the end of the tuple:

## Example:
This example returns the items from 'cherry' and to the end:
```python
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
```
<img width="411" height="43" alt="image" src="https://github.com/user-attachments/assets/03d34acc-2ed1-4389-9479-5aad66e0b7c6" />

## Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the tuple:

## Example:
This example returns the items from index -4(included) to index -1(excluded)
```python
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
```
<img width="245" height="34" alt="image" src="https://github.com/user-attachments/assets/4abd6e87-a58c-41d4-9e8f-96317e9b4f0e" />

## Check if Item Exits
To determine if a specified item is present in a tuple use the in keyword:

## Example:
Check if "apple" is present in the tuple:
```python
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
```
<img width="322" height="34" alt="image" src="https://github.com/user-attachments/assets/0cbd8182-0b06-48e3-bc9f-5f924a1c566e" />
