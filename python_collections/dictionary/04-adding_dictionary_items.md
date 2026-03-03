# Add Dictionary Items
Adding an item to the dictionary is done by using a new index key and assigning a value to it:

## Example:
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
```
<img width="686" height="35" alt="image" src="https://github.com/user-attachments/assets/e6650cd9-3083-45d9-ae20-bef04068f5d6" />

## Update Dictionary
The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
The argument must be a dictionary, or an iterable object with key:value pairs.

## Example:
Add a color item to the dictionary by using the update() method:
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)
```
<img width="684" height="44" alt="image" src="https://github.com/user-attachments/assets/181fcd6a-3006-4cfc-968b-762c342389f3" />
