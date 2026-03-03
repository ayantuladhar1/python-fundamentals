# Accessing Items
You can access the items of a dictionary by referring to its key name, inside square brackets:

## Example:
Get the value of the "model" key:
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
```
<img width="74" height="28" alt="image" src="https://github.com/user-attachments/assets/6cb3b68a-0ee0-4b7c-9bc2-9569d79dee2a" />

There is alos a method called get() that will give you the same result:

## Example:
Get the value of the "model" key:
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)
```
<img width="81" height="37" alt="image" src="https://github.com/user-attachments/assets/3962b4eb-1230-44fc-8f56-bb3c693cf754" />

## Get Keys
The keys() method will return a list of all the keys in the dictionary.

## Example:
Get a list of the keys:
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)
```
<img width="386" height="35" alt="image" src="https://github.com/user-attachments/assets/fb2a6ffc-3b70-4bf8-9f7a-67104be4da37" />

The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

## Example:
Add a new line to the original dictionary, and see that the keys gets updated as well:
```python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change
```
