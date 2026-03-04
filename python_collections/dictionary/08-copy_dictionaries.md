# Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, because dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
There are ways to make a copy, one way is to use the built-in Dictionary method copy().

## Example:
Make a copy of a dictionary with the copy() method:
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
```
<img width="517" height="36" alt="image" src="https://github.com/user-attachments/assets/ecb2d3f0-d4f6-4ad8-8b8a-640f1363c62b" />

Another way to make a copy id to use the built-in function dict().

## Example:
Make a copy of a dictionary with the dict() function:
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
```
<img width="523" height="46" alt="image" src="https://github.com/user-attachments/assets/82910280-a003-4479-979a-55fa020b0b6d" />
