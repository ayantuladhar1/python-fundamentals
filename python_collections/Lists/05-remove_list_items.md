# Remove Lists Item
## Remove Specified Item
The remove() method removes the specified item.

## Example:
Remove "banana":
```python
thislist = ["apple", "banana". "cherry"]
thislist.remove("banana")
print(thislist)
```
<img width="171" height="31" alt="image" src="https://github.com/user-attachments/assets/fee5361d-02a3-4b03-bf7c-b12ab0e93574" />

If there are more than one item with the specified value, the remove() method removes the first occurence:
## Example:
Remove the first occurrence of "banana":
```python
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
```
<img width="336" height="37" alt="image" src="https://github.com/user-attachments/assets/39319919-3e0c-4836-a28d-e80ec88edcbc" />

## Remove Specified Index
The pop() method removes the specified index.

## Example:
Remove the second item:
```python
thislist = ["apple", "banana", "cherry"]
thislits.pop()
print(thislist)
```
<img width="183" height="39" alt="image" src="https://github.com/user-attachments/assets/59973940-afb0-46b2-9323-038bcb920352" />

If you do not specify the index, the pop() method removes the last item.

## Example:
Remove the last item:
```python
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
```
<img width="189" height="29" alt="image" src="https://github.com/user-attachments/assets/0340a1c5-3dd2-4eef-8f40-bb2fd91b1346" />

The del keyword also removes the specified index.

## Example:
Remove the first item:
```python
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
```
<img width="190" height="37" alt="image" src="https://github.com/user-attachments/assets/ab64e1a8-fae8-4b5d-a015-44452c0cb641" />

The del keyword can also delete the list completely.

## Example:
Delete the entire list:
```python
thislist = ["apple", "banana", "cherry"]
del thislist
```

The list has been completly removed from the above example

## Clear the List
The clear() method empties the list, the list still remains but it has no content.

## Example:
Clear the list content:
```python
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
```
<img width="24" height="23" alt="image" src="https://github.com/user-attachments/assets/7b0cc004-68ab-4ab3-89ba-4109bff7948e" />
