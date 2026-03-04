# Remove Dictionary Items
There are several methods to remove items from a dictionary:

## Example:
The pop() method removes the item with the specified key name:
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
```
<img width="323" height="40" alt="image" src="https://github.com/user-attachments/assets/01b6e477-84eb-46ec-bc12-0d68266bd063" />

## Example:
The popitem() method removes the last inserted item:
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
```
<img width="378" height="40" alt="image" src="https://github.com/user-attachments/assets/421fa1ee-7e02-45a1-a312-bcb52a42114d" />

## Example:
The del keyword removes the item with the specified key name:
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
```
<img width="318" height="37" alt="image" src="https://github.com/user-attachments/assets/357b6f45-2eb4-4ba4-a61f-c08734d758c9" />

## Example:
The del keyword can also delete the dictionary completely:
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.
```
<img width="828" height="124" alt="image" src="https://github.com/user-attachments/assets/7aa0355a-adc1-443d-873a-5ffb27be7a9f" />

## Example:
The clear() method empties the dictionary:
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
```
<img width="35" height="31" alt="image" src="https://github.com/user-attachments/assets/83d602d7-02ef-43db-9a7f-64f1c3c20188" />
