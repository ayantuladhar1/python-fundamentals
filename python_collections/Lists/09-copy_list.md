# Copy Lists
## Copy a List
You cannot copy a list simply by typing list2 = list1, because list2 will only be a reference to list1, and changes made in list1 will automatically 
also be made in list2.

## Use the copy() method
You can use the built-in List method copy() to copy a list.

## Example:
Make a copy of a list with the copy() method"
```python
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
```
<img width="254" height="30" alt="image" src="https://github.com/user-attachments/assets/f2fe43ce-5cee-4111-995f-4b9944445e2b" />

## Use the list() method
Another way to make a copy is to use the built-in method list().

## Example:
Make a copy a list with the list() method:
```python
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
```
<img width="258" height="31" alt="image" src="https://github.com/user-attachments/assets/2ecfd1ea-2e2e-4054-ad3d-d5c0ba60e4bd" />

## Use the slice Operator
You can also make a copy of a list by using the : (slice) operator.

## Example:
Make a copy of a list with : operator:
```python
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
```
<img width="261" height="31" alt="image" src="https://github.com/user-attachments/assets/a3ef7f0f-8a3c-4adc-99f8-98a7751e93e7" />
