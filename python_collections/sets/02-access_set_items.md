# Access Set Items
You cannot access items in a set by referring to an index or key.
But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

## Example:
Loop through the set and print the values:
```python
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
```
<img width="65" height="72" alt="image" src="https://github.com/user-attachments/assets/08e4a104-9bde-424b-934f-276d74b949e9" />

## Example:
Check if "banana" is present in the set:
```python
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
```
<img width="45" height="29" alt="image" src="https://github.com/user-attachments/assets/b98e3f3c-4c1c-4b40-ace1-561041a721be" />

## Example:
Check if "banana" is NOT present in the set:
```python
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)
```
<img width="52" height="32" alt="image" src="https://github.com/user-attachments/assets/c71937aa-5a74-4ebb-b000-02bb9520e039" />
