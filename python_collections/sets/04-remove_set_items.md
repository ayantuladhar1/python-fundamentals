# Remove Set Items
To remove an item in a set, use the remove(), or the discard() method.

## Example:
Remove "banana" by using the remove() method:
```python
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
```
<img width="171" height="31" alt="image" src="https://github.com/user-attachments/assets/666b31a9-7296-4c35-bb4c-c46d500e48f6" />

Note: If the item to remove does not exist, remove() will raise an error.

## Example:
Remove "banana" by using the discard() method:
```python
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
```
<img width="173" height="31" alt="image" src="https://github.com/user-attachments/assets/e9102948-60ef-43f5-a079-c7c4b10aff03" />

Note: If the tem item to remove does not exist, discard() will NOT raise an error.

You can also use the opo() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
The return value of the pop() method is the removed item.

## Example:
Remove a random item by using the opo() method:
```python
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal
```
<img width="178" height="60" alt="image" src="https://github.com/user-attachments/assets/3bb86ed9-124c-4448-9f55-5a76cb2db536" />

Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

## Example:
The clear() method empties the set:
```python
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
```
<img width="57" height="31" alt="image" src="https://github.com/user-attachments/assets/e8b63f63-0077-4bc2-aa08-e44c72cdc612" />

## Example:
The del keyword will delete the set completely:
```python
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #this will raise an error because the set no longer exists
```
<img width="702" height="122" alt="image" src="https://github.com/user-attachments/assets/935c444e-22bc-43df-b079-8059316486e4" />
