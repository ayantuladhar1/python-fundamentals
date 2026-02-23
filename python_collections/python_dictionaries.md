# Dictionary items are ordered, changeable, and does not allow duplicates.
* Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["brand"])
```
<img width="62" height="46" alt="image" src="https://github.com/user-attachments/assets/9d63ddac-c118-4f7c-a9c5-902c2e8d2487" />

* Print the number of items in the dictionary:
```python
print(len(thisdict))
```
<img width="18" height="25" alt="image" src="https://github.com/user-attachments/assets/bd9431a3-37df-4943-aefc-257fe5c136f7" />

# Using the dict() method to make a dictionary
```python
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
```
<img width="511" height="40" alt="image" src="https://github.com/user-attachments/assets/79b3ef96-3293-4b18-9576-80591646ff47" />

# Get the value of the "model" key
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
```
<img width="86" height="27" alt="image" src="https://github.com/user-attachments/assets/41aee93a-f40f-4394-b521-ad85279cb217" />

# Get Keys
* The keys() method will return a list of all the keys in the dictionary.
* Add a new item to the original dictionary, and see that the keys list gets updated as well:
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
<img width="503" height="55" alt="image" src="https://github.com/user-attachments/assets/f5584e85-ac14-4ac6-be0b-18fa1c269b3d" />

# Get a list of the values
```python
x = thisdict.values()
```
<img width="413" height="33" alt="image" src="https://github.com/user-attachments/assets/cf4d68db-fcc6-4daa-bdbc-a9de9e71e09d" />

# Make a change in the original dictionary, and see that the values list gets updated as well
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

# Get a list of the key:value pairs
```python
x = thisdict.items()
```
<img width="739" height="28" alt="image" src="https://github.com/user-attachments/assets/516ad496-38b3-4fe5-90ce-4f952bee50e5" />

* Check if "model" is present in the dictionary:
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
```
<img width="633" height="41" alt="image" src="https://github.com/user-attachments/assets/b42cdc31-c055-44c1-b0ae-1bc0a5e49358" />

# The pop() method removes the item with the specified key name
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
```
<img width="343" height="47" alt="image" src="https://github.com/user-attachments/assets/761bab8a-3f84-4681-afa4-d99c19dc7112" />

# The del keyword can also delete the dictionary completely
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict)
```

# The clear() method empties the dictionary
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
```
<img width="32" height="48" alt="image" src="https://github.com/user-attachments/assets/a9b2f2b1-d0d3-423d-97a2-61ceb438a8e0" />

* Print all key names in the dictionary, one by one:
```python
for x in thisdict:
  print(x)
```
<img width="67" height="68" alt="image" src="https://github.com/user-attachments/assets/96d7375a-336f-4cec-b2dd-4345d03d685a" />

* Print all values in the dictionary, one by one:
```python
for x in thisdict:
  print(thisdict[x])
```
<img width="89" height="72" alt="image" src="https://github.com/user-attachments/assets/3baa04e8-5b9a-4926-ba36-f1281e8e6ae2" />

# You can also use the values() method to return values of a dictionary:
```python
for x in thisdict.values():
  print(x)
```
<img width="84" height="76" alt="image" src="https://github.com/user-attachments/assets/76517efc-f458-4ff1-9e7b-427af6160702" />

# You can use the keys() method to return the keys of a dictionary:
```python
for x in thisdict.keys():
  print(x)
```
<img width="68" height="82" alt="image" src="https://github.com/user-attachments/assets/57cc66d6-afa7-49f0-af37-86daec19dea8" />

# Loop through both keys and values, by using the items() method:
```python
for x, y in thisdict.items():
  print(x, y)
```
<img width="158" height="74" alt="image" src="https://github.com/user-attachments/assets/12fcd0f0-5e3f-4a4f-a59c-cb5abb0c2a9e" />

# Make a copy of a dictionary with the copy() method:
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
```
<img width="541" height="43" alt="image" src="https://github.com/user-attachments/assets/edbe0159-13f2-4b23-8fe3-00e97d75ea2e" />

# Make a copy of a dictionary with the dict() function:
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
```
<img width="551" height="36" alt="image" src="https://github.com/user-attachments/assets/338d2be1-f300-4392-be93-0f670a221594" />
