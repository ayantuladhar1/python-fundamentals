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

## Get Values
The values() method will return a list of all the values in the dictionary.

## Example:
Get a list of the values:
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x)
```
<img width="388" height="38" alt="image" src="https://github.com/user-attachments/assets/3cb22812-b7ea-462e-bc4e-af5e5c6fc6a0" />

The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.

## Example:
Make a change in the original dictionary, and see that the values list gets updated as well:
```python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change
```
<img width="394" height="62" alt="image" src="https://github.com/user-attachments/assets/07183950-4693-4036-8060-dd65f86b2c7d" />

## Example:
Add a new item to the original dictionary, and see that the values list gets updated as well:
```python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change
```
<img width="465" height="63" alt="image" src="https://github.com/user-attachments/assets/d0a1d1c0-cc64-462e-bbf0-4fd904b5ab7f" />

## Get Items
The items() method will return each item in a dictionary, as tuples in a list.

## Example:
Get a list of the key:value pairs:
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x)
```
<img width="704" height="38" alt="image" src="https://github.com/user-attachments/assets/346cd57b-c34e-4ea4-87de-97a7fdbf2082" />

The returned list is a view of items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.

## Example:
Make a change in the original dictionary, and see that the items lists gets updated as well:
```python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change
```
<img width="705" height="61" alt="image" src="https://github.com/user-attachments/assets/4716e6b1-e634-4a6f-aab2-3d735876dd2c" />

## Example:
Add a new item to the original dictionary, and see that the item list gets updated as well:
```python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change
```
<img width="894" height="60" alt="image" src="https://github.com/user-attachments/assets/b417444f-1f0f-4608-868e-59d227bbdb65" />

## Check if Key Exists
To determine if a specified key is present in a dictionary use the in keyword:

## Example:
Check if ""
