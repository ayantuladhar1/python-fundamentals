# Join Lists
## Join Two Lists
There are several ways to join, or concentrate, two or more lists in Python.
One of the easiest ways by using the + operator.

## Example:
Join two list:
```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
```
<img width="212" height="33" alt="image" src="https://github.com/user-attachments/assets/a79ff945-96bb-404f-bd92-ac295e7e28ba" />

Another way to join two lists is by appending all the items from list2 into list1, one by one:

## Example:
Append list2 into list1:
```python
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)
```
<img width="218" height="36" alt="image" src="https://github.com/user-attachments/assets/6428ad99-e60d-4fd3-add2-5495d3c8d1e9" />

Or you can use the extend() method, where the purpose is to add elements from one list to another list:

## Example:
Use the extend() method where the purpose is to add elements from one list to another list:
```python
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
```
<img width="218" height="33" alt="image" src="https://github.com/user-attachments/assets/957c2186-9d55-4e20-af04-f9a0daa7dd1e" />
