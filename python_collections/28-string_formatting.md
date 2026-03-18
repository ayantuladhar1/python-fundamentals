# Python String Formatting
F-String was introduced in Python 3.6, and is now the preferred way if formatting strings.
Before Python3.6 we had to use the format() method.

## F-Strings
F-String allows you to format selected parts of a string.
To specify a string as an f-string, simply put an f in front of the string literal, like this:

## Example:
Create an f-string:
```python
txt = f"The price is 49 dollars"
print(txt)
```
<img width="211" height="33" alt="image" src="https://github.com/user-attachments/assets/dcb0c48c-8f5e-4142-851d-8944c74a8190" />

## Placeholders and Modifiers
To format values in an f-string, add placeholders {}, a placeholder can contain variables, operations, functions, and modifiers to format the value.

## Example:
Add a placeholder for the price variable:
```python
price = 59
txt = f"The price is {price} dollars"
print(txt)
```
<img width="213" height="33" alt="image" src="https://github.com/user-attachments/assets/45ee33e0-3d7a-476c-abcc-b7206adfc1f9" />
