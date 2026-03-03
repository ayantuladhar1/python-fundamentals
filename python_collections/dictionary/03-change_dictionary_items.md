# Change Dictionary Items
You can change the value of a specific item by referring to its key name:

## Example:
Change the "year" to 2018:
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
```
<img width="529" height="48" alt="image" src="https://github.com/user-attachments/assets/3f85316d-bb8d-4340-b7a2-2acf8949deba" />

## Update Dictionary
The update() method will update the dictionary with the items from the given argument.
The argumet must be a dictioanry, or an iterable object will key:value pairs.

## Example:
Update the "year" of the car by using the update() method:
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)
```
<img width="523" height="37" alt="image" src="https://github.com/user-attachments/assets/4569b25b-36c5-4e98-9cc2-07ddb09b5ecd" />
