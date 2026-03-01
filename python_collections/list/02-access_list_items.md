# Access List Items
List items are indexed and you can access them by referring to the index number:

## Example:
Print the second items of the list.
```python
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
```
<img width="66" height="23" alt="image" src="https://github.com/user-attachments/assets/c2f84a98-98ec-47e1-9e96-ae8ea1ed5672" />

Note: The first item has index 0.

## Negative Indexing
Negative indexing means start from the end.
-1 refers to the last item, -2 referes to the second last item. etc.

## Example:
Print the last item of the list:
```python
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
```
<img width="62" height="24" alt="image" src="https://github.com/user-attachments/assets/7e8732a4-5193-476f-84e7-9e66691037bd" />

## Ranges of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items.

## Example:
Return the third, fourth and fifth item:
```python
thislits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
```
<img width="257" height="31" alt="image" src="https://github.com/user-attachments/assets/bd31e2ee-f5cb-4d85-809b-581b9ec3a828" />

Note: The search will start at index 2 (including) and end at index 5 (not included)
Remeber that the first item has index 0
By leaving out the start value, the range will start at the firt item:

## Example:
This example returns items from the beginning to, but NOT including, "kiwi":
```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
```
<img width="361" height="41" alt="image" src="https://github.com/user-attachments/assets/9d441f8d-ce08-44fc-8af3-661c6a21aa72" />

Remeber This will return the items from index 0 to index 4. 
Index 0 is the first item and index 4 is the fifth item and index 4 is not included.

## Example:
This example returns the items from "cherry" to the end.
```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
```
<img width="412" height="35" alt="image" src="https://github.com/user-attachments/assets/9a3173d2-621a-46d0-b013-bf5053ba4eb5" />

This will return the items from index 2 to the end.
Remember that index 0 is the first item, index 2 is the third.

## Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the list.

## Example:
This example returns the items from "orange" (-4)t to, but NOT including "mango" (-1):
```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
```
<img width="243" height="35" alt="image" src="https://github.com/user-attachments/assets/5c5bea77-b731-444c-9ef2-e6f0f52d51ad" />

## Check if Item Exists
To determine if a specified item is present in a list use the in keyword:

## Example:
Check if "apple" is present in a list:
```python
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruit list")
```
<img width="310" height="36" alt="image" src="https://github.com/user-attachments/assets/8a178bfe-394a-4b1c-8df9-89c597850251" />
