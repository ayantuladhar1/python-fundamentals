# Unpack Tuple
When we create a tuple, we normally assign values to it. Thi is called "packing" a tuple:

## Example:
Packing a tuple:
```python
fruits = ("apple", "banana", "cherry")
print(fruits)
```
<img width="301" height="48" alt="image" src="https://github.com/user-attachments/assets/c5812918-5631-4f90-a44a-a3b7ab992d22" />

But in Python, we are alos allowed to extend the values back into variables. This is called "unpacking""

## Example:
Unpacking a tuple:
```python
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
```
<img width="81" height="93" alt="image" src="https://github.com/user-attachments/assets/2f1d59fc-752c-4e14-b419-3067a0a3ef38" />

Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

## Using Asterisk *
If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

## Example:
Assign the rest of the values as a list called "red":
```python
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
```
<img width="394" height="96" alt="image" src="https://github.com/user-attachments/assets/24844d1c-9683-48a1-853a-1488fd83d4e2" />

If the asterisk is added to another variable name than the last, Python will assign values to the variable until the bumber of values left matches the number of variables left.

## Example:
Add a list of values the "tropic" variable:
```python
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
```
<img width="343" height="91" alt="image" src="https://github.com/user-attachments/assets/d2636693-745c-4bbb-97af-5c11278221c8" />
