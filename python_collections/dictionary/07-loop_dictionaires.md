# Loop Through a Dictionary
You can loop through a dictionary by using a for loop.
When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values a well.

## Example:
Print all key names in the dictionary, one by one:
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
```
<img width="66" height="90" alt="image" src="https://github.com/user-attachments/assets/bc841c4e-9e7d-4dd8-ac6c-2fa4d1c955db" />

## Example:
Print all values in the dictionary, one by one:
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])
```
<img width="81" height="99" alt="image" src="https://github.com/user-attachments/assets/625f5f86-404b-491e-adeb-b0a047d7c49c" />

## Example:
You can also use the values() method to return values of a dictionary:
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
```
<img width="86" height="90" alt="image" src="https://github.com/user-attachments/assets/a6d5a177-9d71-4532-9c89-33e13d7faaae" />

## Example:
You can also use the keys() method to return the keys of a dictionary:
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)
```
<img width="69" height="92" alt="image" src="https://github.com/user-attachments/assets/2e142293-bcfb-4457-b6b7-3c65c192fe28" />

## Example:
Loop through both keys and values, by using the items() method:
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
```
<img width="143" height="94" alt="image" src="https://github.com/user-attachments/assets/ab614d18-b8e5-4be5-beaa-40399cb92ae9" />
