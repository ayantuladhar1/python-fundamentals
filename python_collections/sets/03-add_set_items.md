# Add Items
Once a set is created, you cannot change its items, but you can add new items.
To add one item to a set use the add() method.

## Example:
Add an item to set, using the add() method:
```python
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
```
<img width="354" height="37" alt="image" src="https://github.com/user-attachments/assets/cde71533-b487-44e5-8508-56dbbf9ebbfd" />

## Add Sets
To add items from another set into tthe current set, use the update() method.

## Example:
Add elements from tropical into thisset:
```python
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
```
<img width="541" height="36" alt="image" src="https://github.com/user-attachments/assets/7a5f7f5d-bf8a-4203-9ed2-d5de77f5242a" />

## Add Any Iterable
The object in the update() method does not have to be a set, it can be any iterable object(tuples, lists, dictionaries etc.).

## Example:
Add elements of a list to a set:
```python
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
```
<img width="419" height="36" alt="image" src="https://github.com/user-attachments/assets/657e6810-dd40-435b-82b0-463fc1356ed9" />
