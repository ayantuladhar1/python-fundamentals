# Python None
None is a special constant in Python that represents the absence of a value.
Its data type is NoneType, and None is the only instance of a NoneType object.

## None type
Variables can be assigned None to indicate "no value" or "no set".

## Example:
```python
x = None
print(x)
```
<img width="44" height="32" alt="image" src="https://github.com/user-attachments/assets/6adc1abc-1a9a-4f46-ad60-5b1488648baf" />

Use type() to see the type of a None value.

## Example:
Assign and print the data type of a None value:
```python
x = None
print(type(x))
```
<img width="168" height="28" alt="image" src="https://github.com/user-attachments/assets/d9735c46-8683-412b-a1a1-a9fb3dd7f19e" />

## Comparing to None
To compare a value to None, use the identity operator is or is not

## Example:
Use the identity operator is for comparisons with None:
```python
result = None
if result is None:
  print("No result yet")
else:
  print("Result is ready")
```
<img width="122" height="26" alt="image" src="https://github.com/user-attachments/assets/11cbc761-ffe2-4141-9374-cb98a7bd7243" />

## Example:
Similar example, but using is not instead:
```python
result = None
if result is not None:
  print("Result is ready")
else:
  print("No result yet")
```
<img width="124" height="21" alt="image" src="https://github.com/user-attachments/assets/c7b46013-530a-470b-8a0a-02df04dbbdf9" />

## Ture or False
None evaluates to False in a boolean context.

## Example:
Check truthiness:
```python
print(bool(None))
```
<img width="53" height="29" alt="image" src="https://github.com/user-attachments/assets/69a142f5-08d6-4c48-9364-f9911da76ba3" />

## Functions returning None
Functions that do not explicitly return a value return None by default.

## Example:
A function without a return statement returns None:
```python
def myfunc():
  x = 5
x = myfunc()
print(x)
```
<img width="48" height="32" alt="image" src="https://github.com/user-attachments/assets/b45c851a-d69f-4fe5-8b99-c2eb02d5a43f" />
